#include <Arduino.h>
#include <LiquidCrystal.h>

#define SERIAL_BUFFER_SIZE 100
// LCD module connections (RS, E, D4, D5, D6, D7)
LiquidCrystal lcd(2, 3, 4, 5, 6, 7);

String serialData = "";

void setup(){
    lcd.begin(20,3);
    Serial.begin(9600);
    
    lcd.setCursor(0,0);
    lcd.print("waiting...");
}

void loop(){
    if(Serial.available()){
        char c = Serial.read();

        if(c == '\n'){
            displayData();
            serialData = "";
        }
        else
            serialData += c;
    }
}

void displayData(){
    uint8_t dateTimeSplit = serialData.indexOf(' ');
    uint8_t tempSplitIndex = serialData.indexOf(',');
    if(dateTimeSplit < 0 || tempSplitIndex < 0) return;
    
    String date = serialData.substring(0,dateTimeSplit);
    String time = serialData.substring(dateTimeSplit+1, tempSplitIndex);
    String temp = serialData.substring(tempSplitIndex + 1, serialData.length());

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Date: " + date);

    lcd.setCursor(0,1);
    lcd.print("Time: " + time);
    
    lcd.setCursor(0,2);
    lcd.print("Temp: " + temp);
}


