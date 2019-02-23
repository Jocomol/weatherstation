import sqlite3
import logging

# Setup
logging.basicConfig(
    filename='/var/log/weatherstation.log', level=logging.DEBUG)
logger = logging.getLogger("Config")
connection = sqlite3.connect('/var/weatherstation/data/wheater.db')
cursor = connection.cursor()

# Read out config from database
cursor.execute('SELECT max(id) FROM config')
max_id = cursor.fetchone()[0]
config = cursor.execute('SELECT * FROM config WHERE ID = ?', str(max_id))
print(config)
