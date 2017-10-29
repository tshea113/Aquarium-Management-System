import serial
import time

arduino = serial.Serial('COM3',9600, timeout=.1)
time.sleep(2)
	
feedFish = ""

while (feedFish != "exit"):
	feedFish = input("Press f to feed fish!\n")
	feedFish = feedFish.lower();

	if (feedFish == "f"):
		print("Writing to arduino!")
		arduino.write(b'f')
	elif (feedFish != "exit"):
		print("Error: Invalid Input!\n")
