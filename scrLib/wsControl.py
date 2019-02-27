# Imports
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
        self.thermo = Thermo(self.thermometer_logger)
        self.db_connector = DBConnector(self.db_connector_logger)
        self.controller_logger.info("All Objects created")

    def main(self):  # Calls all methods and writes results into the database
        data_array = self.thermo.read_measurement()
        self.db_connector.database_insert_measurement(data_array)


if __name__ == "__main__":
    controller = Controller()
    controller.main()
