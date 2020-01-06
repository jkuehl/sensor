#!/usr/bin/python3
import smbus2
import bme280
import mysql.connector

port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

# SQL connection details.
connection = mysql.connector.connect(
	host = "localhost",
	user = "sensor",
	password = "sensor",
	database = "sensor",
	port = 3306 )

# Switch pointer.
cur = connection.cursor(buffered=True)

# Insert data to database.
cur.execute("INSERT INTO sensor_data (LOCATION, DATE, TEMP, PRESSURE, HUMIDITY) VALUES (%s, CURRENT_TIMESTAMP, %s, %s, %s)", ('wohnzimmer', data.temperature, data.pressure, data.humidity))

# Commit changes to database.
connection.commit()

# Close pointer.
cur.close()

# Close connection.
connection.close()
