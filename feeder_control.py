import serial
import time

#Setup the serial port for the arduino
arduino = serial.Serial('COM3',9600, timeout=.1)
time.sleep(2)

#Holds the users command
feedFish = ""

while (feedFish != "exit"):
	feedFish = input("Press f to feed fish!\n")
	feedFish = feedFish.lower();

	if (feedFish == "f"):
		print("Writing to arduino!")
		arduino.write(b'f')
		
		
		
	elif (feedFish != "exit"):
		print("Error: Invalid Input!\n")
	
	if (arduino.inwaiting() > 0):
		arduinoCmd = arduino.read();
		
		if (arduinoCmd == 'd'):
			temp = time.localtime(time.time())
			
			feedTime = ""
			feedTime = feedTime + temp[1] + "/" + temp[2] + "/" temp[0] + " " + temp[3] + ":" + temp[4] + "\n"
			
			arduino.write(feedTime)