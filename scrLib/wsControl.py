##Imports
import datetime
from thermo import thermo
from dbConnector import dbConnector
import pytemperature

##Create Objects
thermo = thermo()
dbConnector = dbConnector()

def tempMeassure():
    tempData = thermo.read()
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

def control():
    dataArray = []
    dataArray.append(getTime())
    dataArray.append(tempMeassure())
    dbConnector.DBInsertMeasurement(dataArray)

def getTime():
    now = datetime.datetime.now()
    return str(now.isoformat())

##TESTING
for i in range(10):
    control()
##
