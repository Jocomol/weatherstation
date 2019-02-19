class WsPart(object): ##This is a superclass for the classes thermo and dbConnector

    def __init__(self, name, logger): #Every wsPart (Wheaterstation Part) has a name and a refrence to the logger
        self.logger = logger
        self.name = name

    def getName(self):
        return self.name
