# This is a superclass for the classes thermo and dbConnector
class WsPart(object):

    # Every wsPart has a name and a refrence to the logger
    def __init__(self, logger):
        self.logger = logger
