##Imports
from thermo import thermo
import pytemperature

##Create Objects
thermo = thermo()

def tempMeassure():
    tempData = thermo.read()
    #TODO Parse and Calculate K, F
	value1 = tempData.split("\n")
	value2 = value1[1]
	value3 = value2.split(" ")
	value4 = value3[9]
	value5 = value4.split("=")
	temp = float(value5[1])
    cel = temp / 1000
    fah = pytemperature.c2f(cel)
    kel = pytemperature.k2c(cel)
    temparray = [cel, fah, kel]
    return temparray

def control():
    print(tempMeassure())


control()
