##Writes into the database very simple
import sqlite3
from wsPart import wsPart
class dbConnector(wsPart):
    def __init__(self, name, logger):
        super().__init__(name, logger)

    def DBInsertMeasurement(self, dataArray):
        conn = sqlite3.connect('/var/wheaterstation/data/wheater.db')
        c = conn.cursor()
        c.execute('insert into measurement (DateTime, temperature_C, temperature_F, temperature_K) VALUES (?,?,?,?)', dataArray)
        self.logger.writeLog(sender=self, message = str('Write',dataArray,'into Database'))
        conn.commit()
        conn.close()
