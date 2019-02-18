##Imports
import datetime
from thermo import thermo
from dbConnector import dbConnector
from logger import logger
from wsPart import wsPart
import pytemperature

class controller():

    name = ""
    Logger = None
    Thermo = None
    DbConnector = None

    def __init__(self):
        ##THis created the controller and all the other objects
        self.name = "Controller"
        ##Create Objects
        self.Logger = logger()
        self.Logger.writeLog(self,"logger created")
        self.Thermo = thermo("Thermometer", self.Logger)
        self.DbConnector = dbConnector("DBConnector", self.Logger)

    def tempMeassure(self):
        ##executed thermo.read and parses the data
        tempData = self.Thermo.read()
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
        ##gets all the data, puts it in arrays and gives id dbConnector
        self.Logger.writeLog(self, "Meassuring started")
        dataArray = []
        dataArray.append(self.getTime())
        tempArray = self.tempMeassure()
        self.Logger.writeLog(self, "Meassured Temperatures:",tempArray[0],tempArray[1],tempArray[2],"write into database soon")
        dataArray.append(tempArray[0])
        dataArray.append(tempArray[1])
        dataArray.append(tempArray[2])
        self.DbConnector.DBInsertMeasurement(dataArray)

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
