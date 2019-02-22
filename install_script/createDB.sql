CREATE TABLE measurement (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
DateTime TEXT,
temperature_C REAL,
temperature_K REAL,
temperature_F REAL
);

CREATE TABLE config (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
intervalMeasurementTime_day REAL,
intervalMeasurementTime_hour REAL,
intervalMeasurementTime_minute REAL,
intervalMeasurementTime_second REAL,
updateInterval_day REAL,
updateInterval_hour REAL,
updateInterval_minute REAL,
updateInterval_second REAL
);

/*
IDEAS:
1: Hardware Info (Name, Manufacturer etc. )
*/
