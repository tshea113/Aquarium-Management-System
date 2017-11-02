/**
   Automated Fish Feeder

   Feeds fish using an auger style fish feeder.
   28BYJ-48 stepper motor controlled using a ULN003 driver on pins 6,7,8,9.
   LCD display on pins 2,3,4,5,11,12 displays the last feed times as well as the feeder status.

   Created 10/21/17
   By Tyler Shea
*/



#include <AccelStepper.h>
#include <LiquidCrystal.h>
#define HALFSTEP 8

// Motor pin definitions
#define motorPin1  6     // IN1
#define motorPin2  7     // IN2
#define motorPin3  8     // IN3
#define motorPin4  9     // IN4

//Initialize the stepper motor
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);

//Initialize the LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

//Define the buttons
int FEED_BUTTON = 10;
int DISPLAY_BUTTON = 13;

//Used for turning the display off and on
bool isDisplayOn = true;

//Holds the time of last feed cycle in format "MM/DD/YYYY HH:MM"
String lastFeedTime = "";

void setup()
{
  //Set the motor params
  stepper1.setMaxSpeed(500.0);
  stepper1.setAcceleration(200.0);

  //Set the dimensions of the LCD
  lcd.begin(16, 2);

  //Set the button input
  pinMode(FEED_BUTTON, INPUT);
  pinMode(DISPLAY_BUTTON, INPUT);

  //Set up the serial connection
  Serial.begin(9600);

  lcd.print("Ready to feed!");
}

void loop()
{
  //Feeds if the button is pressed
  if (digitalRead(FEED_BUTTON) == HIGH)
  {
    feed();

    lcd.print("Last fed at:");
    lastFeedTime = getTime();
    lcd.setCursor(0, 1);
    lcd.print(lastFeedTime);
  }

  //Switches the display on and off
  if (digitalRead(DISPLAY_BUTTON) == HIGH)
  {
    isDisplayOn = displayFeedTime(lastFeedTime, isDisplayOn);
    delay(500);
  }

  //Also feed if pi triggers
  else if (Serial.available() > 0)
  {
    char data = Serial.read();
    if (data == 'f')
    {
      feed();
    }
    Serial.flush();

    lcd.print("Last fed at:");
    lastFeedTime = getTime();
    lcd.setCursor(0, 1);
    lcd.print(lastFeedTime);
  }
}

/**
   This operates the fish feeder
   Turns the stepper motor for 1 feeding cycle
*/
void feed()
{
  lcd.clear();
  stepper1.moveTo(4096);  //Set the desired stopping point for the feeding cycle. TODO: Determine the length of the feeding cycle.

  //Runs the feeding cycle
  lcd.print("Feeding...");
  while (stepper1.distanceToGo() != 0)
  {
    stepper1.run();
  }

  //Reset the stepper home for next feeding cycle
  lcd.clear();
  stepper1.setCurrentPosition(0);
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
      lcd.print("Not fed!");
    }
    else
    {
      lcd.print("Last fed at:");
      lcd.setCursor(0,1);
      lcd.print(lastFeedTime);
    }
    return isDisplayOn;
  }
}

/**
 * Retrieves the datetime string from the pi
 */
String getTime()
{
  String feedTime;

  Serial.write('d');

  delay(10);

  while (Serial.available() > 0)
  {
    feedTime = Serial.readString();
  }

  Serial.flush();
  return feedTime;
}

