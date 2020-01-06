#!/usr/bin/python3
import sys
import Adafruit_DHT
import mysql.connector

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

# SQL connection details.
connection = mysql.connector.connect(
	host = "192.168.0.227",
	user = "sensor",
	password = "sensor",
	database = "sensor",
	port = 3306 )

# Switch pointer.
cur = connection.cursor(buffered=True)

# Insert data to database.
cur.execute("INSERT INTO sensor_data (LOCATION, DATE, TEMP, PRESSURE, HUMIDITY) VALUES (%s, CURRENT_TIMESTAMP, %s, %s, %s)", ('3ddrucker', temperature, '', humidity))

# Commit changes to database.
connection.commit()

# Close pointer.
cur.close()

# Close connection.
connection.close()
