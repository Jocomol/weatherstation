##Imports
from thermo import thermo

##Create Objects
thermo = thermo()

def tempMeassure():
    tempData = thermo.read()
    #TODO Parse and Calculate K, F
    return tempData

def control():
    print(tempMeassure())


control()
