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
const int LEFT_BUTTON = 10;
const int MID_BUTTON = 11;
const int RIGHT_BUTTON = 12;

//Define the rotation settings
const int TWO_TURN = -8192;
const int ONE_TURN = -4096;
const int HALF_TURN = -2048;
const int QUARTER_TURN = -1024;

int rotations = ONE_TURN;

// Setup the menu
// 0(feed), 1(rotations)
int menu = 0;

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
  pinMode(LEFT_BUTTON, INPUT_PULLUP);
  pinMode(MID_BUTTON, INPUT_PULLUP);
  pinMode(RIGHT_BUTTON, INPUT_PULLUP);

  //Set up the serial connection
  Serial.begin(9600);

  //Handshake to establish serial connection
  while (1)
  {
	delay(1000);
	Serial.print('r');
	delay(1000);
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
  // Cycle through the menus
  if (digitalRead(RIGHT_BUTTON) == LOW)
  {
    delay(50);
    if (digitalRead(RIGHT_BUTTON) == HIGH)
    {
      if (menu < 1) menu++;
      else menu = 0;
      printMenu(menu, lastFeedTime, rotations);
    }
  }
  
  // Feed the fish
  if (digitalRead(LEFT_BUTTON) == LOW && menu == 0)
  {
    delay(50);
    if (digitalRead(LEFT_BUTTON) == HIGH)
    {
    lastFeedTime = feed(rotations);
    }
  }

  // Switch the display on and off
  if (digitalRead(MID_BUTTON) == LOW)
  {
    delay(50);
    if (digitalRead(MID_BUTTON) == HIGH)
    {
      isDisplayOn = displayToggle(lastFeedTime, rotations, isDisplayOn, menu); 
    }
  }

  // Choose between different feed amounts
  if (digitalRead(LEFT_BUTTON) == LOW && menu == 1)
  {
    delay(50);
    if (digitalRead(LEFT_BUTTON) == HIGH)
    {
      switch(rotations)
      {
        case TWO_TURN:
          rotations = QUARTER_TURN;
          break;
        case ONE_TURN:
          rotations = TWO_TURN;
          break;
        case HALF_TURN: 
          rotations = ONE_TURN;
          break;
        case QUARTER_TURN:
          rotations = HALF_TURN;
          break;  
      }
      printMenu(menu, lastFeedTime, rotations); 
    }
  }
  
  //Also feed if pi triggers
  if (Serial.available() > 0)
  {
    char data = Serial.read();
    
    //f requests a feed cycle
    if (data == 'f')
    {
      lastFeedTime = feed(rotations);
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
String feed(int rotations)
{
  //Retrieve the feed time from the pi
  String lastFeedTime = getTime();
  
  lcd.clear();

  //Set the desired stopping point for the feeding cycle. 
  //TODO: Determine the length of the feeding cycle.
  stepper1.moveTo(rotations);  

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
   This toggles the display on and off
*/
bool displayToggle(String lastFeedTime, int rotations, bool isDisplayOn, int menu)
{
  //Turn the display off if it is on
  if (isDisplayOn)
  {
    lcd.noDisplay();
    lcd.setBacklight(LOW);
    isDisplayOn = false;

    return isDisplayOn;
  }
  //Otherwise turn the display on and display the menu
  else
  {
    lcd.display();
    lcd.clear();
    isDisplayOn = true;
    printMenu(menu, lastFeedTime, rotations);
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
        if (Serial.peek() == 't') 
		{
			Serial.read();
			feedTime = Serial.readStringUntil('\n');
		}
		else feedTime = "Invalid Signal!";
  }
     
  return feedTime;
}

/**
 * Prints the current menu
 */
void printMenu(int menu, String lastFeedTime, int rotations)
{
  lcd.clear();
  // Feed menu
  if (menu == 0)
  {
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
  }
  // Rotations menu
  else if (menu == 1)
  {
    lcd.print("Feed Amount:");
    lcd.setCursor(0,1);
    switch(rotations)
    {
      case TWO_TURN:
        lcd.print("Two Turns");
        break;
      case ONE_TURN:
        lcd.print("One turn");
        break;
      case HALF_TURN: 
        lcd.print("Half turn");
        break;
      case QUARTER_TURN:
        lcd.print("Quarter turn");
        break;  
    }
  }
}

