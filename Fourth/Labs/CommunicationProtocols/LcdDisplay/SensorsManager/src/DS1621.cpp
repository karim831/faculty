#include "DS1621.hpp"


void DS1621::init(){
    Wire.beginTransmission(DS1621_ADDRESS);
    Wire.write(DS1621_Config_ADDRESS);
    Wire.write(0x00);

    Wire.beginTransmission(DS1621_ADDRESS);
    Wire.write(DS1621_Start_ADDRESS);
    Wire.endTransmission();
}


void DS1621::readTemp(){
    Wire.beginTransmission(DS1621_ADDRESS);
    Wire.write(DS1621_Temp_ADDRESS);
    Wire.endTransmission(false);

    Wire.requestFrom(DS1621_ADDRESS,2);
    
    if(Wire.available() >= 2){
        Temp = Wire.read();
        if(Wire.read() & 0x80)
            Temp += .5;
    }
}

String DS1621::toString(){
    return String(Temp) + "C";
}