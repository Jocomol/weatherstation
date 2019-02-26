import sqlite3
import logging

# Setup
logging.basicConfig(
    filename='/var/log/weatherstation.log', level=logging.DEBUG)
logger = logging.getLogger("Config")
connection = sqlite3.connect('/var/weatherstation/data/weather.db')
cursor = connection.cursor()

# Read out config from database
cursor.execute("""SELECT * FROM config WHERE
    ID = (SELECT MAX(ID) FROM config);""")
config = cursor.fetchone()
connection.close()
print("Current Config:")
print("time_measureInterval:")
print("- weekday: " + str(config[1]))
print("- month: " + str(config[2]))
print("- day: " + str(config[3]))
print("- hour: " + str(config[4]))
print("- minute: " + str(config[5]))
print("")
print("time_updateInterval:")
print("- weekday: " + str(config[6]))
print("- month: " + str(config[7]))
print("- day: " + str(config[8]))
print("- hour: " + str(config[9]))
print("- minute: " + str(config[10]))

logger.info("showed Config")
