import os, sys
from wsPart import wsPart
class thermo:
    functional = False
    file = '/sys/bus/w1/devices/28-00000833e8ff/w1_slave'
    def __init__(self, name, logger):
        super(name, logger).__init__()
        functional = True

    def read(self):
        fileobject = open(self.file)
        filecontent = fileobject.read()
        fileobject.close()
        self.logger.writeLog(self,"Completed Meassurement")
        return filecontent
