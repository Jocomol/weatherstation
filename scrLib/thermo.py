import os
importsys
from wsPart import WsPart


class Thermo(WsPart):  #Reads out the file of the data from the Thermometer
    functional = False  #Functionality will be added later
    #File where the thermometer writes the data in
    file = '/sys/bus/w1/devices/28-00000833e8ff/w1_slave'
    #file = "/home/joco/Documents/testing.txt"
    
    def __init__(self, name, logger):
        super().__init__(name, logger)  #Calls the wsPart constructor

    def read_measurement(self):  #Reads out the file defined as self.file
        with open(self.file) as fileobject:
            fileobject = open(self.file)
            filecontent = fileobject.read()
            fileobject.close()
            self.logger.info("Completed Meassuring")
        return filecontent
