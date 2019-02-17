
class object:
    logger = None
    name = ""
    def __init__(self, name, logger):
        self.logger = logger
        self.name = name
        self.logger.writeLog(self, "created")

    def getName(self):
        return self.name
