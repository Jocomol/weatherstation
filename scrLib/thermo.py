import os, sys, time

class thermo:
    functional = False
    file = '/sys/bus/w1/devices/28-00000833e8ff/w1_slave'
    def __init__(self):
        ##Run test to see if functional
        functional = True

    def read(self):
        fileobject = open(self.file)
        filecontent = fileobject.read()
        fileobject.close()
        return filecontent
