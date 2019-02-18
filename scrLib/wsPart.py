##This is a superclass for the classes thermo and dbConnector
class WsPart(object):
    #Logger = None
    #name = ""
    def __init__(self, name, logger):
        self.logger = logger
        self.name = name
        self.logger.writeLog(self, "created")

    def getName(self):
        return self.name
