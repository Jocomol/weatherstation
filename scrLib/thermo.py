import os, sys
from wsPart import WsPart
class Thermo(WsPart):
    functional = False ## see line 8
    file = '/sys/bus/w1/devices/28-00000833e8ff/w1_slave' ##File where the thermometer writes the datas in
    def __init__(self, name, logger):
        super().__init__(name, logger) ## this calls the wsPart constructor
        self.functional = True ##will implement a self test later, currently this line does nothing

    def read_measurement(self):
        ##reads out the file mentioned in line 5 and returns it
        with open(self.file) as fileobject:
            fileobject = open(self.file)
            filecontent = fileobject.read()
            fileobject.close()
            self.logger.writeLog(self,"Completed Meassurement")
        return filecontent
