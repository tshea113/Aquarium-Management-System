/**
   Automated Fish Feeder

   Feeds fish using an auger style fish feeder.
   28BYJ-48 stepper motor controlled using a ULN003 driver on pins 6,7,8,9.
   LCD display on pins 2,3,4,5,11,12 displays the last feed times as well as the feeder status.

   Created 10/21/17
   By Tyler Shea
*/



#include <AccelStepper.h>
#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#define HALFSTEP 8

// Motor pin definitions
#define motorPin1  6     // IN1
#define motorPin2  7     // IN2
#define motorPin3  8     // IN3
#define motorPin4  9     // IN4

//Initialize the stepper motor
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);

//Initialize the LCD
LiquidCrystal_I2C lcd(0x3F,2,1,0,4,5,6,7);

//Define the buttons
int FEED_BUTTON = 10;
int DISPLAY_BUTTON = 11;

//Used for turning the display off and on
bool isDisplayOn = true;

//Holds the time of last feed cycle in format "MM/DD/YYYY HH:MM"
String lastFeedTime = "";

void setup()
{
  //Set the motor params
  stepper1.setMaxSpeed(700.0);
  stepper1.setAcceleration(200.0);

  //Set the dimensions of the LCD
  lcd.setBacklightPin(3,POSITIVE);
  lcd.setBacklight(HIGH);
  lcd.begin(16,2);
  lcd.clear();
  lcd.home();
  

  //Set the button input
  pinMode(FEED_BUTTON, INPUT_PULLUP);
  pinMode(DISPLAY_BUTTON, INPUT_PULLUP);

  //Set up the serial connection
  Serial.begin(9600);

  delay(2000);

  //Handshake to establish serial connection
  Serial.print('r');

  while (1)
  {
    if (Serial.available() > 0)
    {
      if (Serial.read() == 'r')
      {
        break;
      }
    }
  }
  
  //Setup Confirmation
  lcd.print("Ready to feed!");
}

void loop()
{
  //Feeds if the button is pressed
  if (digitalRead(FEED_BUTTON) == LOW)
  {
    lastFeedTime = feed();
  }

  //Switches the display on and off
  if (digitalRead(DISPLAY_BUTTON) == LOW)
  {
    isDisplayOn = displayFeedTime(lastFeedTime, isDisplayOn);
    delay(500);
  }

  //Also feed if pi triggers
  if (Serial.available() > 0)
  {
    char data = Serial.read();
    
    //f requests a feed cycle
    if (data == 'f')
    {
      lastFeedTime = feed();
    }

    //d precedes a date string
    if (data == 'd')
    {
      lastFeedTime = Serial.readString();
    }
    
  }
}

/**
   This operates the fish feeder
   Turns the stepper motor for 1 feeding cycle
   Returns the time at which it fed
*/
String feed()
{
  //Retrieve the feed time from the pi
  String lastFeedTime = getTime();
  
  lcd.clear();

  //Set the desired stopping point for the feeding cycle. 
  //TODO: Determine the length of the feeding cycle.
  stepper1.moveTo(-4096);  

  //Runs the feeding cycle
  lcd.print("Feeding...");
  while (stepper1.distanceToGo() != 0)
  {
    stepper1.run();
  }

  //Reset the stepper home for next feeding cycle
  lcd.clear();
  stepper1.setCurrentPosition(0);

  //Print the time of feeding to the lcd
  lcd.print("Last fed at:");
  lcd.setCursor(0, 1);
  lcd.print(lastFeedTime);

  return lastFeedTime;
}

/**
   This prints the last feed time to the LCD
*/
bool displayFeedTime(String lastFeedTime, bool isDisplayOn)
{
  //Turn the display off if it is on
  if (isDisplayOn)
  {
    lcd.noDisplay();
    lcd.setBacklight(LOW);
    isDisplayOn = false;

    return isDisplayOn;
  }
  //Otherwise turn the display on and display last feed time if available
  else
  {
    lcd.display();
    lcd.clear();
    isDisplayOn = true;
    //If the device was just turned on there will be no last feed time
    if (lastFeedTime.equals(""))
    {
      lcd.print("Not fed yet!");
    }
    else
    {
      lcd.print("Last fed at:");
      lcd.setCursor(0,1);
      lcd.print(lastFeedTime);
    }
    lcd.setBacklight(HIGH);
    return isDisplayOn;
  }
}

/**
 * Retrieves the datetime string from the pi
 */
String getTime()
{
  String feedTime = "";

  //char d used to request the date
  Serial.write('d');
  delay(30);
  
  //Retrieve the date
  //Date is terminated by a newline
  while (Serial.available() > 0)
  {
        char temp = Serial.read();
        if (temp != '\n')
        {
          feedTime += temp;  
        }
  }
      
  return feedTime;
}

