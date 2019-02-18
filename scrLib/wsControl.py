##Imports
import datetime
from thermo import Thermo
from dbConnector import DBConnector
from logger import Logger
from wsPart import WsPart
import pytemperature

class Controller():

    #name = ""
    #Logger = None
    #Thermo = None
    #DbConnector = None

    def __init__(self):
        ##THis created the controller and all the other objects
        self.name = "Controller"
        ##Create Objects
        self.logger = Logger()
        self.logger.writeLog(self,"logger created")
        self.thermo = Thermo("Thermometer", self.Logger)
        self.db_connector = DBConnector("DBConnector", self.Logger)

    def tempMeassure(self):
        ##executed thermo.read and parses the data
        temp_data = self.thermo.read_measurement()
        value_1 = temp_data.split("\n")
        value_2 = value_1[1]
        value_3 = value_2.split(" ")
        value_4 = value_3[9]
        value_5 = value_4.split("=")
        temp = float(value_5[1])
        cel = temp / 1000
        fah = pytemperature.c2f(cel)
        kel = pytemperature.c2k(cel)
        temp_array = [str(cel), str(fah), str(kel)]
        return temp_array

    def control(self):
        ##gets all the data, puts it in arrays and gives id dbConnector
        self.logger.writeLog(self, "Meassuring started")
        data_array = []
        data_array.append(self.getTime())
        temp_array = self.tempMeassure()
        self.logger.writeLog(self, "Meassured Temperatures:",temp_array[0],temp_array[1],temp_array[2],"write into database soon")
        data_array.append(temp_array[0])
        data_array.append(temp_array[1])
        data_array.append(temp_array[2])
        self.db_connector.database_insert_measurement(data_array)

    def getTime(self):
        now = datetime.datetime.now()
        return str(now.isoformat())

    def getName(self):
        return self.name

##TESTING
for i in range(10):
    controller = Controller()
    controller.control()
##
