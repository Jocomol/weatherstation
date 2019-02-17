import os, sys
from wsPart import wsPart
class thermo(wsPart):
    functional = False ## see line 8
    file = '/sys/bus/w1/devices/28-00000833e8ff/w1_slave' ##File where the thermometer writes the datas in
    def __init__(self, name, logger):
        super().__init__(name, logger) ## this calls the wsPart constructor
        functional = True ##will implement a self test later, currently this line does nothing

    def read(self):
        ##reads out the file mentioned in line 5 and returns it
        fileobject = open(self.file)
        filecontent = fileobject.read()
        fileobject.close()
        self.logger.writeLog(self,message="Completed Meassurement")
        return filecontent
