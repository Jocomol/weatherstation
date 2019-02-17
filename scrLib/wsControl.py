##Imports
import datetime
from thermo import thermo
from dbConnector import dbConnector
from logger import logger
from object import object
import pytemperature

class controller():

    name = ""
    logger = None
    thermo = None
    dbConnector = None

    def __init__(self):
        self.name = "Controller"
        ##Create Objects
        self.logger = logger()
        self.logger.writeLog(self, "logger created")
        self.thermo = thermo("Thermometer", logger)
        self.dbConnector = dbConnector("DBConnector",logger)

    def tempMeassure(self):
        tempData = self.thermo.read()
        value1 = tempData.split("\n")
        value2 = value1[1]
        value3 = value2.split(" ")
        value4 = value3[9]
        value5 = value4.split("=")
        temp = float(value5[1])
        cel = temp / 1000
        fah = pytemperature.c2f(cel)
        kel = pytemperature.c2k(cel)
        temparray = [str(cel), str(fah), str(kel)]
        return temparray

    def control(self):
        self.logger.writeLog(self, "Meassuring started")
        dataArray = []
        dataArray.append(getTime())
        tempArray = tempMeassure()
        self.logger.writeLog(self, str("Meassured Temperatures:",tempArray[0],tempArray[1],tempArray[2],"write into database soon"))
        dataArray.append(tempArray[0])
        dataArray.append(tempArray[1])
        dataArray.append(tempArray[2])
        self.dbConnector.DBInsertMeasurement(dataArray)

    def getTime(self):
        now = datetime.datetime.now()
        return str(now.isoformat())

    def getName(self):
        return self.name

##TESTING
for i in range(10):
    controller = controller()
    controller.control()
##
