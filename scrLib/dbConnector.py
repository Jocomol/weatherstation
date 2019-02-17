import sqlite3
from object import object
class dbConnector(object):
    def __init__(self, name, logger):
        super(self, name, logger).__init__()

    def DBInsertMeasurement(self, dataArray):
        conn = sqlite3.connect('/var/wheaterstation/data/wheater.db')
        c = conn.cursor()
        c.execute('insert into measurement (DateTime, temperature_C, temperature_F, temperature_K) VALUES (?,?,?,?)', dataArray)
        self.logger.writeLog(self, str('Write',dataArray,'into Database'))
        conn.commit()
        conn.close()
