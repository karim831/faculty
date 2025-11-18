#include "DS1307.hpp"

uint8_t DS1307::bcdToDec(uint8_t value) {
    return (value / 16 * 10) + (value % 16);
}

uint8_t DS1307::decToBcd(uint8_t value) {
    return (value / 10 * 16) + (value % 10);
}

void DS1307::read() {
    Wire.beginTransmission(DS1307_ADDRESS);
    Wire.write(0x00);
    Wire.endTransmission();

    Wire.requestFrom(DS1307_ADDRESS, 7);

    if (Wire.available() >= 7) {
        currentDateTime.seconds = bcdToDec(Wire.read());
        currentDateTime.minute  = bcdToDec(Wire.read());
        currentDateTime.hour    = bcdToDec(Wire.read());
        Wire.read(); // skip day of week
        currentDateTime.day     = bcdToDec(Wire.read());
        currentDateTime.month   = bcdToDec(Wire.read());
        currentDateTime.year    = bcdToDec(Wire.read());
    }
}

void DS1307::write(DateTime dt) {
    Wire.beginTransmission(DS1307_ADDRESS);
    Wire.write(0x00);

    Wire.write(decToBcd(dt.seconds));
    Wire.write(decToBcd(dt.minute));
    Wire.write(decToBcd(dt.hour & 0b00011111));
    Wire.write(decToBcd(1)); // day-of-week dummy
    Wire.write(decToBcd(dt.day));
    Wire.write(decToBcd(dt.month));
    Wire.write(decToBcd(dt.year));

    Wire.endTransmission();
}


String DS1307::serialize() {
    char data[32];

    snprintf(
        data,
        sizeof(data),
        "%02d %02d %02d %02d %02d %02d",
        currentDateTime.year,
        currentDateTime.month,
        currentDateTime.day,
        currentDateTime.hour,
        currentDateTime.minute,
        currentDateTime.seconds
    );

    return String(data);
}



String DS1307::toString(bool is12Mode = true) {
    String s = "";

    // ---------- DATE ----------
    if (currentDateTime.day < 10) s += "0";
    s += String(currentDateTime.day) + "/";

    if (currentDateTime.month < 10) s += "0";
    s += String(currentDateTime.month) + "/";

    s += String(2000 + currentDateTime.year) + " ";

    // ---------- TIME ----------
    uint8_t hour = currentDateTime.hour;
    String ampm = "";

    if (is12Mode) {
        if (hour == 0) {
            hour = 12;      
            ampm = " AM";
        } 
        else if (hour < 12) {
            ampm = " AM";   
        }
        else if (hour == 12) {
            ampm = " PM";  
        }
        else {
            hour -= 12;    
            ampm = " PM";
        }
    }

    if (hour < 10) s += "0";
    s += String(hour) + ":";

    if (currentDateTime.minute < 10) s += "0";
    s += String(currentDateTime.minute) + ":";

    if (currentDateTime.seconds < 10) s += "0";
    s += String(currentDateTime.seconds);

    s += ampm;

    return s;
}

