##This is a superclass for the classes thermo and dbConnector
class wsPart(object):
    logger = None
    name = ""
    def __init__(self, name, logger):
        self.logger = logger
        self.name = name
        self.logger.writeLog(str(self.getName()), message=str("created"))

    def getName(self):
        return self.name
