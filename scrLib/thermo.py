from wsPart import WsPart
import os
import sys
from w1thermsensor import W1ThermSensor
import datetime


class Thermo(WsPart, W1ThermSensor):

    def __init__(self, logger):
        super().__init__(logger)  # Calls the wsPart constructor
        self.set_precision(5)

    def read_measurement(self):
        self.logger.info("Meassuring started")
        meassuered_data = [str(datetime.datetime.now.().isoformat())]
        meassuered_data.append(self.get_temperatures([
                    self.DEGREES_C,
                    self.DEGREES_F,
                    self.KELVIN]))
        self.thermometer_logger.info(
            "Meassured Temperatures: " +
            str(meassuered_data))
        return meassuered_data
