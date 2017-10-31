import serial
import time
import datetime
import sched

def setFeedTime():
	feedHour = -1
	feedInterval = -1
	while (feedHour < 0 or feedHour > 23):
		print "Enter the hour in 24 hour format at which you wish to first feed the fish:"
		feedHour = input()
		
		if (feedHour < 0 or feedHour > 23):
			print "Error: Invalid hour!"
	
	while (feedInterval < 0):
		print "Enter the desired time interval in hours between feedings:"
		feedInterval = input()
		
		if (feedInterval < 0):
			print "Error: Invalid interval!"
	
	feedParams = [feedHour, feedInterval]
	
	return feedParams

def talkToArduino(arduino):
	#Reads data from the arduino
	arduinoCmd = arduino.read();
			
	#Arduino sends 'd' when it is requesting the time
	if (arduinoCmd == 'd'):
		temp = time.localtime(time.time())
		
		#Formats the time for proper display on arduino LCD
		#MM/DD/YYYY HH:MM
		feedTime = ""
		feedTime = feedTime + str(temp[1]) + "/" + str(temp[2]) + "/" + str(temp[0]) + " " + str(temp[3]) + ":" + str(temp[4])
		
		arduino.write(feedTime)

#Waits for an event to happen and exceutes corresponding effect
def main():
	#Setup the serial port for the arduino
	arduino = serial.Serial('COM3',9600, timeout=.1)
	time.sleep(2)
	
	#Take in the desired feed timer settings
	feedTimer = setFeedTime()
	
	try:
		while (1):
			
			#Checks for a time request from the arduino
			if (arduino.inWaiting() > 0):
				talkToArduino(arduino)
	except KeyboardInterrupt:
		pass		

if __name__ == '__main__': main()