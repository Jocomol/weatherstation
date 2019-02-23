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
    ID = (SELECT MAX(ID)  FROM TABLE);""")
config = cursor.fetchone()
print(config)
connection.close()
