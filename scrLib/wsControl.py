# Imports
import datetime
from thermo import Thermo
from dbConnector import DBConnector
from wsPart import WsPart
import pytemperature
import logging


class Controller():  # Controlls everything and manages the weatherstation

    def __init__(self):  # Creates all the Objects
        logging.basicConfig(
            filename='/var/log/weatherstation.log',
            level=logging.DEBUG)
        self.name = "Controller"
        self.controller_logger = logging.getLogger("Controller")
        self.thermometer_logger = logging.getLogger("Thermometer")
        self.db_connector_logger = logging.getLogger("Database Connector")
        self.thermo = Thermo("Thermometer", self.thermometer_logger)
        self.db_connector = DBConnector(
            "DBConnector",
            self.db_connector_logger)
        self.controller_logger.info("All Objects created")

    # Gets the temparature data from the thermometer class
    def tempMeassure(self):
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

    def main(self):  # Calls all methods and writes results into the database
        self.thermometer_logger.info("Meassuring started")
        data_array = []
        data_array.append(self.getTime())
        temp_array = self.tempMeassure()
        self.thermometer_logger.info(
            "Meassured Temperatures: " +
            str(temp_array))
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
    controller.main()
#
