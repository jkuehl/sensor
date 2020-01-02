
#!/usr/bin/python3
import smbus2
import bme280
import mysql.connector

location = 'wohnzimmer'
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
print(data.id)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# Prepare SQL query to INSERT a record into the ase.
connection = mysql.connector.connect( host = "localhost", user = "sensor", password = "sensor", database = "sensor", port = 3306 )
cur = connection.cursor(buffered=True)

cur.execute("SELECT * FROM sensor_data ORDER BY count DESC LIMIT 1")
rows = cur.fetchall()
for r in rows:
  print(f" count = {r[0]}") # id = {r[1]} date = {r[2]} temp = {r[3]} pressure = {r[4]} humidity = {r[5]}")

cur.execute("INSERT INTO sensor_data (ID, DATE, TEMP, PRESSURE, HUMIDITY) VALUES (%s, %s, %s, %s, %s)", ('data.id', '', '20.811272679554532', '1017.1958053169708', '54.36379026801714',))
connection.commit()
cur.execute("SELECT * FROM sensor_data ORDER BY count DESC LIMIT 1")
rows = cur.fetchall()
for r in rows:
  print(f" count = {r[0]}") # id = {r[1]} date = {r[2]} temp = {r[3]} pressure = {r[4]} humidity = {r[5]}")

#close current.
cur.close()
#close connection.
connection.close()
