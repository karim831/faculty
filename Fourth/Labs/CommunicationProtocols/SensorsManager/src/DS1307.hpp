/**
 * DS1307 is Real Time Clock I2C Support
 * I2C Address is 0x68
 * 
 * Commands:
 * Start from (With Auto Increments after that): 0x00 (seconds Register) => 0x06 (year register) 
 * 
 * Data Retrieved:
 * 7bytes : from seconds to year
*/

#ifndef DS1307_HPP
#define DS1307_HPP

#include <Wire.h>
#include "DateTime.hpp"

class DS1307 {
public:
    DateTime currentDateTime;

    void readDS1307();
    void writeDS1307(DateTime dt);
    String toString(bool is12Mode = true);

private:
    const uint8_t DS1307_ADDRESS = 0x68;

    uint8_t bcdToDec(uint8_t value);
    uint8_t decToBcd(uint8_t value);
};

#endif
