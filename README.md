# Aquarium Management System
## Description:
An aquarium management system powered by Raspberry Pi and Arduino.  Feeds fish in scheduled intervals according to user defined start time and time between feedings as well as at the press of a hardware button.  Able to remotely monitor and change feed schedule from a website hosted on the Raspberry Pi.  More features currently in development.  Planned features include a relay module to monitor water level, light cycling, and temperature overheat protection.

## Parts:
- Arduino
- Raspberry Pi
- 3D printed feeder mechanism
- 2x Pushbutton Switches
- 28BYJ-48 Stepper Motor
- LN003 Motor Driver
- 16x2 LCD with LCM1602 I2C Backpack

## Setup:
### Arduino:

Build the arduino circuit as shown in the included image.  The arduino connects to the RasPi through USB which both powers the arduino as well as serves as the serial connection.  The arduino uses the [Accelstepper](http://www.airspayce.com/mikem/arduino/AccelStepper/) library for the motor and the [NewLiquidCrystal](https://bitbucket.org/fmalpartida/new-liquidcrystal/wiki/Home) for the I2C LCD.

### Raspberry Pi:

The python files will need to be modified for your specific setup.  You will need to modify the file paths for all of the log files if your path is different.  If you decide to use USB for the serial connection, then you may need to modify the serial ID.  All of the imported python libraries can be installed through pip except for the basic authentification library for flask which can be found [here](https://flask-basicauth.readthedocs.io/en/latest/).

### Website:

The website uses the flask microframework and can be hosted in any way you choose.  I chose to use Gunicorn and Nginx because it seemed to be the easiest way that worked the best.
