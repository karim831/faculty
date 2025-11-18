#include <Wire.h>
#include "src/DateTime.hpp"
#include "src/DS1307.hpp"
#include "src/DS1621.hpp"

DS1307 rtc;
DS1621 temp;

uint8_t lastReadMinute = 255;

void setup(){
  Serial.begin(9600);
  Wire.begin();
  temp.init();
}


void loop() {
  rtc.read();

  if(lastReadMinute != rtc.currentDateTime.minute){
    lastReadMinute = rtc.currentDateTime.minute;

    temp.read();
  }
  
  Serial.println(rtc.serialize());
  Serial.println(temp.Temp);
  delay(1000);
}