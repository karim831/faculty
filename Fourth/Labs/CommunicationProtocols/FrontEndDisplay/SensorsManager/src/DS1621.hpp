/**
 * DS1621 Digital Temperature Sensor I2C Support
 * I2C Default Address is 0x48 when A0,A1,A2 assigning to GND
 * Read -55 to +125 with accuracy +.5 represented in two's complement
 * 
 * Commands:
 * init Configuration Register With Mode : 0xAC ->  Modes (Continuous mode 0x00, shot mode 0x01)
 * Start Conversion : 0xEE
 * Read Temperature Register: 0xAA
 * 
 * Data Retrieved:
 * 1byte for integer
 * 1byte for fraction 0x80 if +.5 
 */

#ifndef DS1621_HPP
#define DS1621_HPP

#include <Wire.h>

class DS1621{
    private:
        const uint8_t DS1621_ADDRESS = 0x48;
        const uint8_t DS1621_Config_ADDRESS = 0xAC;
        const uint8_t DS1621_Start_ADDRESS = 0xEE;
        const uint8_t DS1621_Temp_ADDRESS = 0xAA;


    public: 
        float Temp = 0.0;

        void init();
        void read();
        String toString();
};

#endif