##Writes messages into the logfile it gets the name of the sender of the message by executing the getter defined in the superclass wsPart
import datetime
from wsPart import wsPart
class logger():
    logfile = "/var/log/wheaterstation.log"
    name = "Logger"
    def writeLog(sender, message):
        conn = open(self.logfile, "w")
        now = str(datetime.datetime.now().isoformat())
        conn.write("[" + now + "]" + " (" + sender + "): " + message + "\n")
        conn.close()

    ##Cant extend wsPart because every wsPart needs a logger, this is why I added this incase i need its name
    def getName(self):
        return self.name
