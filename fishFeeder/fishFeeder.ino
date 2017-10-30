/**
 * Automated Fish Feeder
 * 
 * Feeds fish using an auger style fish feeder.
 * 28BYJ-48 stepper motor controlled using a ULN003 driver on pins 6,7,8,9.
 * LCD display on pins 2,3,4,5,11,12 displays the last feed times as well as the feeder status.
 * 
 * Created 10/21/17
 * By Tyler Shea
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

int BUTTON = 10;

String lastFeedTime = "";

void setup()
{
  //Set the motor params
  stepper1.setMaxSpeed(500.0);
  stepper1.setAcceleration(200.0);

  //Set the dimensions of the LCD
  lcd.begin(16,2);

  //Set the button input
  pinMode(BUTTON, INPUT);

  //Set up the serial connection
  Serial.begin(9600);

  lcd.print("Ready to feed!");
}

void loop()
{
  //Feeds if the button is pressed
  if (digitalRead(BUTTON) == HIGH)
  {
    feed();

    lcd.print("Last fed at:");
    lastFeedTime = getTime();
    lcd.setCursor(2,0);
    lcd.print(lastFeedTime);
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
    lcd.setCursor(0,2);
    lcd.print(lastFeedTime);
  }
}

/**
 * This operates the fish feeder
 * Turns the stepper motor for 1 feeding cycle
 */
void feed()
{
  lcd.clear();
  stepper1.moveTo(4096);  //Set the desired stopping point for the feeding cycle. TODO: Determine the length of the feeding cycle.

  //Runs the feeding cycle
  lcd.print("Feeding...");
  while(stepper1.distanceToGo() != 0)
  {
    stepper1.run();
  }

  //Reset the stepper home for next feeding cycle
  lcd.clear();
  stepper1.setCurrentPosition(0);
}

/**
 * This prints the last feed time to the LCD
 */
void printFeedTime()
{
  //TODO: Figure out how to get a date/time value sent to the arduino (Possibly through the pi?)  
}

String getTime()
{
  String feedTime = "";
  
  Serial.write('d');

  delay(10);
  
  while (Serial.available() > 0)
  {
    feedTime = Serial.readStringUntil("\n");
  }

  Serial.flush();
  return feedTime;
}

