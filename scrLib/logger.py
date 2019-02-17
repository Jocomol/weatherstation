import datetime
from object import object
class logger():
    logfile = "var/log/wheaterstation.log"
    name = "Logger"
    def writeLog(self, sender, message):
        conn = open(self.logfile)
        now = str(datetime.datetime.now().isoformat())
        conn.write("[" + now + "] " + " (" + sender.getName() + "):" + message + "\n")
        conn.close()

    def getName(self):
        return self.name
