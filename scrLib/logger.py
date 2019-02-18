##Will deleted probably
import datetime
from wsPart import WsPart

class Logger(): ##Writes messages into the logfile it gets the name of the sender of the message by executing the getter defined in the superclass wsPart

    logfile = "/var/log/wheaterstation.log"
    name = "Logger"

    def writeLog(self, sender, message): ##Writes the datetime, the name of the sender and the message into the logfile
        with open(self.logfile, "a") as f:
            now = str(datetime.datetime.now().isoformat())
            f.write("[" + now + "]" + " (" + sender.getName() + "): " + message + "\n")
            f.close()

    def getName(self): ##Can't extend wsPart because every wsPart needs a logger, this is why I added this incase i need its name
        return self.name
