##Writes into the database very simple
import sqlite3
from wsPart import WsPart
class DBConnector(WsPart):
    def __init__(self, name, logger):
        super().__init__(name, logger)

    def database_insert_measurement(self, measurement):
        connection = sqlite3.connect('/var/wheaterstation/data/wheater.db')
        cursor = connection.cursor()
        cursor.execute('insert into measurement (DateTime, temperature_C, temperature_F, temperature_K) VALUES (?,?,?,?)', measurement)
        self.logger.writeLog(self, 'Write ' + str(measurement) + ' into Database')
        connection.commit()
        connection.close()
