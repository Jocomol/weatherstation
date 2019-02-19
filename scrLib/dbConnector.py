import sqlite3
from wsPart import WsPart

class DBConnector(WsPart): ##Writes into the database very simple

    def __init__(self, name, logger):
        super().__init__(name, logger)

    def database_insert_measurement(self, measurement): ##Inserts the mmeasurement data into the database
        connection = sqlite3.connect('/var/wheaterstation/data/wheater.db')
        cursor = connection.cursor()
        cursor.execute('insert into measurement (DateTime, temperature_C, temperature_F, temperature_K) VALUES (?,?,?,?)', measurement)
        self.logger.info("Write: " + str(measurement) + " into database")
        connection.commit()
        connection.close()
