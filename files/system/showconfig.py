import sqlite3
import logging
import colorful

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
print(colorful.bold_underlined("Current Config:"))
print(colorful.bold_green("time_measureInterval:"))
print(colorful.bold("- weekday: ") + str(config[1]))
print(colorful.bold("- month: ") + str(config[2]))
print(colorful.bold("- day: ") + str(config[3]))
print(colorful.bold("- hour: ") + str(config[4]))
print(colorful.bold("- minute: ") + str(config[5]))
print("")
print(colorful.bold_green("time_updateInterval:"))
print(colorful.bold("- weekday: ") + str(config[6]))
print(colorful.bold("- month: ") + str(config[7]))
print(colorful.bold("- day: ") + str(config[8]))
print(colorful.bold("- hour: ") + str(config[9]))
print(colorful.bold("- minute: ") + str(config[10]))

logger.info("showed Config")
