import serial
import time
import datetime
import sched
import os
import threading
import sys

lastFeed = 0.0


# Takes in the feed time and intervals from the users and stores in text file
# Returns a tuple with the hour to feed and time between feedings
def setFeedTime():
	feedHour = -1
	feedInterval = -1
	
	# Hour needs to be in 24 hour format (0 to 23)
	while feedHour < 0 or feedHour > 23:
		print "Enter the hour in 24 hour format at which you wish to first feed the fish:"
		feedHour = input()
		
		if feedHour < 0 or feedHour > 23:
			print "Error: Invalid hour!"
	
	# Cannot have negative interval
	while feedInterval < 0:
		print "Enter the desired time interval in hours between feedings:"
		feedInterval = input()
		
		if feedInterval < 0:
			print "Error: Invalid interval!"
	
	# Save the feed parameters to a text file
	newTimes = str(feedHour) + " " + str(feedInterval)
	with open("/home/pi/fish_feeder/env/fishFeeder/logs/feed_time.txt", "w") as f:
		file.write(newTimes)
	

	feedParams = [feedHour, feedInterval]
	return feedParams


# Sends the feed time to the arduino
def sendTime(arduino):
	global lastFeed 
	lastFeed = time.time()
		
	# Formats the time for proper display on arduino LCD
	# tMM/DD/YYYY HH:MM\n
	# t is the signal bit for a date
	# Newline signals an end of string to arduino
	lastFeedString = ""
	lastFeedString = 't' + time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed)) + '\n'
	
	
	# Send the date to arduino
	arduino.write(lastFeedString)
	
	# Logs the time of the feeding
	with open("/home/pi/fish_feeder/env/fishFeeder/logs/feed_log.txt", "a") as f:
		f.write(time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed)) + "\n")

	# Logs the time of feeding for the website
	with open("/home/pi/fish_feeder/env/fishFeeder/logs/last_feed.txt", "w") as f:
		f.truncate()
		f.write(time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed)))


# Handles requests from the arduino
def talkToArduino(arduino):
	arduinoCmd = 0
	
	# Reads data from the arduino
	if arduino.inWaiting() > 0:
		arduinoCmd = arduino.read()
			
		# Arduino sends 'd' when it is requesting the time
		# This will happen when a manual feed cycle occurs
		if arduinoCmd == 'd':
			sendTime(arduino)
			
		# Arduino sends 'r' when it has been reset
		# Writing 'r' back completes the connection handshake
		if arduinoCmd == 'r':
			arduino.write('r')

				
# Retrieves the feed timer parameters from the text file
def getFeedTimer():
	with open("/home/pi/fish_feeder/env/fishFeeder/logs/feed_time.txt", "r") as f:
		temp = f.read()
	
	temp = temp.split()
	
	feedParams = [int(temp[0]), int(temp[1])]
	return feedParams

# Sends the feed siganl
def feedFish(arduino):
	arduino.write('f')
	return

# Used to check for time requests from arduino in background
def arduinoCheck(arduino):
	while 1:
		if arduino.inWaiting() > 0:
			talkToArduino(arduino)


# Waits for an event to happen and exceutes corresponding effect
def runFeeder():
	# Setup the serial port for the arduino
	windowsPort = 'COM3'	  # Used for windows debugging
	piPort = '/dev/ttyUSB0'	  # Used on the pi
	
	arduino = serial.Serial(piPort, 9600, timeout=.1)
	
	# Confirm connection to the arduino
	arduinoConnected = False
	while not arduinoConnected:
		if arduino.inWaiting() > 0:
			temp = arduino.read()
			if temp == 'r':
				arduinoConnected = True
				arduino.write('r')
	
	s = sched.scheduler(time.time, time.sleep)
	
	# Thread that checks for time requests from arduino
	t = threading.Thread(name='arduinoCheck', target=arduinoCheck, args=(arduino,))
	t.daemon = True
	t.start()
	
	# Get the timer params
	feedTimer = getFeedTimer()
	

	# Create a feed log if it doesn't exist
	if not os.path.exists("/home/pi/fish_feeder/env/fishFeeder/logs/feed_log.txt"):
		f = open("/home/pi/fish_feeder/env/fishFeeder/logs/feed_log.txt", "w")
		f.close()
	
	# Setup the last feed text file for the website if it doesn't exist
	if not os.path.exists("/home/pi/fish_feeder/env/fishFeeder/logs/last_feed.txt"):
		f = open("/home/pi/fish_feeder/env/fishFeeder/logs/last_feed.txt", "w")
		f.write("N/A")
		f.close()

	# Setup the next feed time file for the website if it doesn't exist
	if not os.path.exists("/home/pi/fish_feeder/env/fishFeeder/logs/next_feed.txt"):
		f = open("/home/pi/fish_feeder/env/fishFeeder/logs/next_feed.txt", "w")
		f.write("N/A")
		f.close()

	# Runs the feeder
	while 1:
			
		currHour = datetime.datetime.now().hour
		currMinute = datetime.datetime.now().minute
			
		# Sets the feed timer for later in the day if it is after the current time
		if int(feedTimer[0]) > currHour:
			feedDelta = (60 * (int(feedTimer[0]) - currHour)) - currMinute
		
		# Otherwise set it for the next day
		else:
			feedDelta = (60 * ((24 - currHour) + feedTimer[0])) - currMinute
		
		# feedDelta holds the number of minutes from the current time to feed
		# timeToFeed is the absolute time in seconds to feed
		timeToFeed = (time.time() + (feedDelta * 60))
		s.enterabs(timeToFeed, 1, feedFish, (arduino,))

		# Logs the next feed time for the website
		with open("/home/pi/fish_feeder/env/fishFeeder/logs/next_feed.txt", "w") as f:
			f.truncate()
			f.write(time.strftime("%m/%d/%y %H:%M",time.localtime(timeToFeed)))

		s.run()
		
		while 1:		
			# If the feeding has occurred, set for next interval
			if not s.queue:
				#Check for any changes in the feed schedule
				feedTimer = getFeedTimer()
			
				feedDelay = int(feedTimer[1]) * 3600
				s.enter(feedDelay, 1, feedFish, (arduino,))
				
				# Logs the next feed time for the website
				with open("/home/pi/fish_feeder/env/fishFeeder/logs/next_feed.txt", "w") as f:
					f.truncate()
					f.write(time.strftime("%m/%d/%y %H:%M",time.localtime(time.time() + feedDelay)))
				
				s.run()
					




if __name__ == '__main__':
	runFeeder()
