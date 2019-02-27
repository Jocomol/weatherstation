import sqlite3
from wsPart import WsPart


class DBConnector(WsPart):  # Writes into the database very simple

    def __init__(self, logger):
        super().__init__(logger)

    # Inserts the mmeasurement data into the database
    def database_insert_measurement(self, measurement):
        connection = sqlite3.connect('/var/weatherstation/data/weather.db')
        cursor = connection.cursor()
        cursor.execute("""
            insert into measurement (
                DateTime,
                temperature_C,
                temperature_F,
                temperature_K)
            VALUES (?,?,?,?)""", measurement)
        self.logger.info("Write: " + str(measurement) + " into database")
        connection.commit()
        connection.close()
