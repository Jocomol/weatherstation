#This is a superclass for the classes thermo and dbConnector
class WsPart(object):

    #Every wsPart has a name and a refrence to the logger
    def __init__(self, name, logger):
        self.logger = logger
        self.name = name

    def getName(self):
        return self.name
