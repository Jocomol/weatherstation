##Writes into the database very simple
import sqlite3
from wsPart import WsPart
class DBConnector(WsPart):
    def __init__(self, name, logger):
        super().__init__(name, logger)

    def database_insert_measurement(self, measurement):
        try:
            connection = sqlite3.connect('/var/wheaterstation/data/wheater.db')
            cursor = connection.cursor()
            cursor.execute('insert into measurement (DateTime, temperature_C, temperature_F, temperature_K) VALUES (?,?,?,?)', dataArray)
            self.logger.writeLog(self, str('Write',measurement,'into Database'))
        except Exception as e:
            print(e.message)
        finally:
            connection.commit()
            connection.close()
