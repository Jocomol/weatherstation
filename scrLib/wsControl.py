##Imports
import datetime
from thermo import Thermo
from dbConnector import DBConnector
from logger import Logger
from wsPart import WsPart
import pytemperature

class Controller(): #Controlls everything and manages the Wheaterstation

    def __init__(self): ##Creates all the Objects
        self.name = "Controller"
        self.logger = Logger()
        self.logger.writeLog(self,"logger created")
        self.thermo = Thermo("Thermometer", self.logger)
        self.db_connector = DBConnector("DBConnector", self.logger)

    def tempMeassure(self): ##Gets the temparature data from the thermometer class
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

    def main(self): ##Calls all methods and writes results into the database
        self.logger.writeLog(self, "Meassuring started")
        data_array = []
        data_array.append(self.getTime())
        temp_array = self.tempMeassure()
        self.logger.writeLog(self, "Meassured Temperatures: " + str(temp_array[0]) + str(temp_array[1]) + str(temp_array[2]) + " write into database soon")
        data_array.append(temp_array[0])
        data_array.append(temp_array[1])
        data_array.append(temp_array[2])
        self.db_connector.database_insert_measurement(data_array)

    def getTime(self):
        now = datetime.datetime.now()
        return str(now.isoformat())

    def getName(self):
        return self.name


if __name__ == "__main__":
    controller = Controller()
##TESTING
    for i in range(10):
        controller.main()
##
