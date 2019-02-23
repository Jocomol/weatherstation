CREATE TABLE measurement (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
DateTime TEXT,
temperature_C REAL,
temperature_K REAL,
temperature_F REAL
);

CREATE TABLE config (
ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
time_measureInterval_weekday REAL,
time_measureInterval_month REAL,
time_measureInterval_day REAL,
time_measureInterval_hour REAL,
time_measureInterval_minute REAL,
time_updateInterval_weekday REAL,
time_updateInterval_month REAL,
time_updateInterval_day REAL,
time_updateInterval_hour REAL,
time_updateInterval_minute REAL
);

/*
IDEAS:
1: Hardware Info (Name, Manufacturer etc. )
*/
