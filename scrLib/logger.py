##Writes messages into the logfile it gets the name of the sender of the message by executing the getter defined in the superclass wsPart
import datetime
from wsPart import WsPart
class Logger():
    logfile = "/var/log/wheaterstation.log"
    name = "Logger"
    def writeLog(self, sender, message):
        with open(self.logfile, "a") as f:
            now = str(datetime.datetime.now().isoformat())
            f.write("[" + now + "]" + " (" + sender.getName() + "): " + message + "\n") ##gets the name of the sender and the message and writes it into the logfile
            f.close()

    ##Cant extend wsPart because every wsPart needs a logger, this is why I added this incase i need its name
    def getName(self):
        return self.name
