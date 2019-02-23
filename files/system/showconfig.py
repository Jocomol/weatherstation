import sqlite3
import logging

# Setup
logging.basicConfig(
    filename='/var/log/weatherstation.log', level=logging.DEBUG)
logger = logging.getLogger("Config")
connection = sqlite3.connect('/var/weatherstation/data/wheater.db')
cursor = connection.cursor()

# Read out config from database
cursor.execute("""SELECT * FROM config WHERE
    ID = (SELECT MAX(ID) FROM config);""")
config = cursor.fetchone()
connection.close()
print("Current Config:")
print("time_measureInterval:")
print("- weekday: " + config[1])
print("- month: " + config[2])
print("- day: " + config[3])
print("- hour: " + config[4])
print("- minute: " + config[5])
print("")
print("time_updateInterval:")
print("- weekday: " + config[6])
print("- month: " + config[7])
print("- day: " + config[8])
print("- hour: " + config[9])
print("- minute: " + config[10])
