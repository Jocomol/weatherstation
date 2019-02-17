import sqlite3

class dbConnector:
    def DBInsertMeasurement(self, dataArray):
        connection = sqlite3.connect('/var/wheaterstation/data/wheater.db')
        c = conn.cursor()
        c.execute('insert into measurement (DateTime, temperature_C, temperature_F, temperature_K) VALUES (?,?,?,?)', dataArray)
        conn.commit()
        conn.close()
