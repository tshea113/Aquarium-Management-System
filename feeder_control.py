import serial
import time
import datetime
import sched
import os

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

def talkToArduino(arduino):
	#Reads data from the arduino
	arduinoCmd = arduino.read();
			
	#Arduino sends 'd' when it is requesting the time
	if (arduinoCmd == 'd'):
		lastFeed = time.time()
		
		#Formats the time for proper display on arduino LCD
		#MM/DD/YYYY HH:MM
		lastFeedString = ""
		lastFeedString = time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed))
		
		arduino.write(lastFeedString)
		
		return lastFeed

def findNextFeed(feedHour):
	
	#TODO: Might use this to find the next feed time
	pass

#Retrieves the feed timer parameters from the text file
def getFeedTimer():
	with open("feed_time.txt", "r") as file:
		temp = file.read()
	
	temp.split()
	
	feedParams = [temp[0], temp[1]]
	return feedParams
	
#Waits for an event to happen and exceutes corresponding effect
def main():
	#Setup the serial port for the arduino
	arduino = serial.Serial('COM3',9600, timeout=.1)
	time.sleep(2)
	
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
	lastFeed = 0
	
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
			
			try:
				while (1):
					#Checks for a time request from the arduino
					if (arduino.inWaiting() > 0):
						lastFeed = talkToArduino(arduino)
						
						#Logs the time of the feeding
						with open("feed_log.txt", "a") as file:
							file.write(time.strftime("%m/%d/%y %H:%M",time.localtime(lastFeed)) + "\n")
						
					#TODO: Use scheduler to feed at desired interval/time
					
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