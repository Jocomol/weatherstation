##This is a superclass for the classes thermo and dbConnector
class wsPart(object):
    Logger = None
    name = ""
    def __init__(self, name, Logger):
        self.Logger = Logger
        self.name = name
        self.Logger.writeLog(self, "created")

    def getName(self):
        return self.name
