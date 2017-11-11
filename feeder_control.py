import serial
import time
import datetime
import sched
import os

lastFeed = 0.0

#Takes in the feed time and intervals from the users and stores in text file
#Returns a tuple with the hour to feed and time between feedings
def setFeedTime():
	feedHour = -1
	feedInterval = -1
	
	#Hour needs to be in 24 hour format (0 to 23)
	while (feedHour < 0 or feedHour > 23):
		print "Enter the hour in 24 hour format at which you wish to first feed the fish:"
		feedHour = input()
		
		if (feedHour < 0 or feedHour > 23):
			print "Error: Invalid hour!"
	
	#Cannot have negative interval
	while (feedInterval < 0):
		print "Enter the desired time interval in hours between feedings:"
		feedInterval = input()
		
		if (feedInterval < 0):
			print "Error: Invalid interval!"
	
	#Save the feed parameters to a text file
	newTimes = str(feedHour) + " " + str(feedInterval)
	with open("feed_time.txt", "w") as file:
		file.write(newTimes)
	

	feedParams = [feedHour, feedInterval]
	return feedParams

#Sends the feed time to the arduino
def sendTime(arduino):
	global lastFeed 
	lastFeed = time.time()
		
	#Formats the time for proper display on arduino LCD
	#MM/DD/YYYY HH:MM
	lastFeedString = ""
	lastFeedString = time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed))
	arduino.write(lastFeedString)
	
	#Logs the time of the feeding
	with open("feed_log.txt", "a") as file:
		file.write(time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed)) + "\n")
	
def talkToArduino(arduino):
	#Reads data from the arduino
	arduinoCmd = arduino.read();
			
	#Arduino sends 'd' when it is requesting the time
	if (arduinoCmd == 'd'):
		sendTime(arduino)

def findNextFeed(feedHour):
	
	#TODO: Might use this to find the next feed time
	pass

#Retrieves the feed timer parameters from the text file
def getFeedTimer():
	with open("feed_time.txt", "r") as file:
		temp = file.read()
	
	temp = temp.split()
	
	feedParams = [int(temp[0]), int(temp[1])]
	return feedParams

def feedFish(arduino):
	arduino.write('f')
	return talkToArduino(arduino)
	
#Waits for an event to happen and exceutes corresponding effect
def main():
	#Setup the serial port for the arduino
	arduino = serial.Serial('COM3',9600, timeout=.1)
	time.sleep(2)
	
	s = sched.scheduler(time.time, time.sleep)
	
	#Create feeding schedule if it doesn't exist
	if not os.path.exists("feed_time.txt"):
		feedTimer = setFeedTime()
	
	else:
		feedTimer = getFeedTimer()
	
	#Create a feed log if it doesn't exist
	if not os.path.exists("feed_log.txt"):
		file = open("feed_log.txt", "w")
		file.close()	
	
	userInput = 0
	
	print "#######################\nMain Menu:\n#######################\n1)Change Feed Timer\n2)Last Feed Time\n3)Start Feed Timer\n4)Exit\n#######################"
	
	#Runs the menu for the program until the user decides to exit
	while (userInput != 4):
		
		userInput = input("Option: ");
	
		#Changes the feeder's feeding time and time between feedings
		if (userInput == 1):
			feedTimer = setFeedTime()
	
		#Prints the last feed time if it exists
		if (userInput == 2):
			if (lastFeed != 0):
				print ("Last fed at: " + time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed))) 
			
			else:
				print ("Fish not fed yet!")
			
		#This puts the feeder in standby until scheduled feed time
		if (userInput == 3):
			print "Feeder is active!"
			
			currHour = datetime.datetime.now().hour
			
			#Sets the feed timer for later in the day if it is after the current time
			if (int(feedTimer[0]) > currHour):
				feedDelta = int(feedTimer[0]) - currHour
			
			#Otherwise set it for the next day
			else:
				feedDelta = ((24 - currHour) + feedTimer[0])
			
			timeToFeed = time.time() + (feedDelta * 3600)
			print "Next feed time:", time.asctime(time.localtime(timeToFeed))
			s.enterabs(timeToFeed, 1, feedFish, (arduino,))
			s.run()
			
			try:
				while (1):
					#Checks for a time request from the arduino
					#TODO: Fix issue with date not being sent while scheduler is waiting.
					if (arduino.inWaiting() > 0):
						print "Sending date!"
						talkToArduino(arduino)
												
					#If the feeding has occurred, set for next interval
					if not s.queue:
						feedDelay = feedTimer[1] * 3600
						s.enter(feedDelay, 1, feedFish, (arduino,))
						print "Next feed time in", feedTimer[1], "hours." 
						s.run()
						
			except KeyboardInterrupt:
				pass
				
			print "Feeder is no longer active!"
			
		#Exit the program
		if (userInput == 4):
			break
			
		#Handles garbage input	
		if (userInput < 1 or userInput > 4):
			print "Error: Invalid Input!"
if __name__ == '__main__': main()