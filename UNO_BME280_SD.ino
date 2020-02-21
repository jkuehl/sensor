/***************************************************************************
UNO + BME280 + SD
 ***************************************************************************/

#include <Wire.h>
#include <SPI.h>
#include <SD.h>

#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)
Adafruit_BME280 bme;

const int chipSelect = 4;

void setup() {
    Serial.begin(9600);
//    while (!Serial) {
//      ; // wait for serial port to connect. Needed for native USB port only
//    }

    Serial.print("Initializing SD card.");
    if (!SD.begin(chipSelect)) {
      Serial.println("Card failed, or not present."); // don't do anything more:
      while (1);
      }
    Serial.println("card initialized.");
    

    Serial.println(F("Initializing BME280."));
    if (! bme.begin(0x76, &Wire)) {
        Serial.println("Could not find a valid BME280 sensor, check wiring!");
        while (1);
    }

    File dataFile = SD.open("datalog.txt", FILE_WRITE);
    if (dataFile) {
      dataFile.println("temperature,pressure,altitude,humidity");
      dataFile.close();
    }
    else {
      Serial.println("Init error opening datalog.txt");
    }

    Serial.println("temperature,pressure,altitude,humidity");
}


void loop() {
    String dataString = "";
    dataString += String(bme.readTemperature());
    dataString += ",";
    dataString += String(bme.readPressure() / 100.0F);
    dataString += ",";
    dataString += String(bme.readAltitude(SEALEVELPRESSURE_HPA));
    dataString += ",";
    dataString += String(bme.readHumidity());
    
    File dataFile = SD.open("datalog.txt", FILE_WRITE);
    if (dataFile) {
      dataFile.println(dataString);
      dataFile.close();
    }
    else {
      Serial.println("Loop error opening datalog.txt");
    }    

    Serial.println(dataString);

    delay(5000);
}