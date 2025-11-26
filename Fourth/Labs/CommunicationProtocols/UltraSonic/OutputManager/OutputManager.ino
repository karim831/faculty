#include <Arduino.h>
#include <Servo.h>
#include <LiquidCrystal.h>

Servo motor;
LiquidCrystal lcd(2,3,4,5,6,7);

String buffer = "";
int angle = 0;

void setup(){
    Serial.begin(9600);
    motor.attach(9); // PWM pin
    motor.write(0);
    lcd.begin(20, 4);

    lcd.setCursor(0,0);
    lcd.print("System Ready");
    delay(1000);
}

void loop(){
    if(Serial.available()){
        char c = Serial.read();

        if(c == '\n'){
            parseData();
            buffer = "";
        }
        else{
            buffer += c;
        }
    }
}

void parseData(){
    int dateTimeIndex = buffer.indexOf(' ');
    int commaIndex = buffer.indexOf(',');
    if(commaIndex < 0 || dateTimeIndex < 0) return;

    String dateStr = buffer.substring(0, dateTimeIndex);
    String timeStr = buffer.substring(dateTimeIndex+1, commaIndex);
    int openFlag = buffer.substring(commaIndex + 1).toInt();

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("date: " + dateStr);

    lcd.setCursor(0,1);
    lcd.print("time: " + timeStr);

    if(openFlag == 1)
        motor.write((angle = (angle + 90) % 270)); // 0 -> 180 

    
    lcd.setCursor(0,2);
    lcd.print("Servo: " + String(angle) + "deg");
}
