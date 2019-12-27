#!/usr/bin/python3
import smbus2
import bme280
import pymysql

sensor = 'wohnzimmer'
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
print(data.id)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# Prepare SQL query to INSERT a record into the ase.
connection = pymysql.connect("localhost","sensor","sensor","sensor" )
cursor = connection.cursor()

try:
  sql.execute("""INSERT INTO sensor_data (ID, TEMP, PRESSURE, HUMIDITY)
              VALUES ('data.id', 'data.temperature', 'data.pressure', 'data.humidity')""")
  print ("execute to database")
  connection.commit()
  print ("commit to database")
  connection.close()

except:
  # Rollback in case there is any error
  connection.rollback()
  print("rollback")

connection.close()


