import serial
import time

#Setup the serial port for the arduino
arduino = serial.Serial('COM3',9600, timeout=.1)
time.sleep(2)

#Holds the users command
feedFish = ""

while (feedFish != "exit"):
	feedFish = raw_input("Press f to feed fish!\n")
	feedFish = feedFish.lower();

	if (feedFish == "f"):
		print "Writing to arduino!"
		arduino.write(b'f')
		
		
		
	elif (feedFish != "exit"):
		print "Error: Invalid Input!\n"
	
	if (arduino.inWaiting() > 0):
		print "Attempting to read the data!"
		arduinoCmd = arduino.read();
		
		if (arduinoCmd == 'd'):
			temp = time.localtime(time.time())
			
			feedTime = ""
			feedTime = feedTime + str(temp[1]) + "/" + str(temp[2]) + "/" + str(temp[0]) + " " + str(temp[3]) + ":" + str(temp[4]) + "\n"
			
			print feedTime
			
			arduino.write(feedTime)