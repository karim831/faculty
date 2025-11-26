#include <Wire.h>
#include "src/DS1307.hpp"

DS1307 rtc;
uint8_t lastSec = 255;
uint8_t counter = 0;
void setup(){
    Serial.begin(9600);
    Wire.begin();
}

void loop(){
    rtc.readDS1307();

    uint8_t sec = rtc.currentDateTime.seconds;

    if(sec != lastSec){
        lastSec = sec;

        String timeStr = rtc.toString(); // 12H Mode
        bool shouldOpen = ((counter = (++counter % 5)) == 0);   // each 5 seonds and reset counter

        Serial.print(timeStr);
        Serial.print(",");
        Serial.println(shouldOpen ? 1 : 0);
    }

    delay(50);
}
