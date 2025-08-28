# // Pin Definitions
const int irSensorPin = 2;   // IR Sensor input pin
const int buzzerPin  = 3;   // Buzzer output pin
const int gsmTx      = 10;  // GSM Module Tx pin
const int gsmRx      = 11;  // GSM Module Rx pin

#include <SoftwareSerial.h>   // Library for serial communication

SoftwareSerial gsmSerial(gsmTx, gsmRx); // Create a software serial for GSM

void setup() {
  pinMode(irSensorPin, INPUT);   // IR Sensor as input
  pinMode(buzzerPin, OUTPUT);    // Buzzer as output

  Serial.begin(9600);            // Serial monitor for debugging
  gsmSerial.begin(9600);         // Serial communication with GSM

  Serial.println("System Ready...");
  sendSMS("GeoFencing System is Active.");
}

void loop() {
  int irSensorValue = digitalRead(irSensorPin);

  // Check if IR sensor detects an obstacle
  if (irSensorValue == LOW) { // IR sensor output goes LOW when triggered
    Serial.println("Intrusion Detected!");
    digitalWrite(buzzerPin, HIGH);   // Activate buzzer

    sendSMS("Alert! Intrusion detected in the farm.");
    makeCall();

    delay(5000);   // Wait for 5 seconds before resetting
    digitalWrite(buzzerPin, LOW);   // Deactivate buzzer
  }
}

// Function to send SMS
void sendSMS(String message) {
  gsmSerial.println("AT+CMGF=1");          // Set SMS mode to text
  delay(1000);
  gsmSerial.println("AT+CMGS=\"+1234567890\""); // Replace with recipient's phone number
  delay(1000);
  gsmSerial.print(message);
  delay(1000);
  gsmSerial.write(26);  // End of message (CTRL+Z)
  delay(1000);

  Serial.println("SMS Sent.");
}

// Function to make a call
void makeCall() {
  gsmSerial.println("ATD+1234567890;");  // Replace with recipient's phone number
  delay(10000);                          // Call for 10 seconds
  gsmSerial.println("ATH");              // Hang up
  Serial.println("Call Made.");
}
