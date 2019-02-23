# Jocomol/weatherstation/scrLib
This is the script library wich manages the weatherstation.

## Files

### dbConnector.py
The connector from the scrLib to the database.

### thermo.py
The representation of the thermometer in the scrLib. Reads out the data from the thermometer.

### wsControl.py
This class is the management class of the weatherstation.

### wsPart.py
The superclass of all the parts of the weatherstation

#### Subclasses
- thermo.py
- dbConnector.py
