# WIP
from crontab import CronTab
import yaml
import logging
import sqlite3

# Setup
logging.basicConfig(
    filename='/var/log/wheaterstation.log',level=logging.DEBUG)
logger = logging.getLogger("Config")
crontab = CronTab(user='root')
connection = sqlite3.connect('/var/wheaterstation/data/wheater.db')
cursor = connection.cursor()

# Load configfile
with open("/var/wheaterstation/config.yml", 'r') as stream:
    try:
        yamlconfig = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        logger.error("Error occured appling the config " + exc)

# Cronjob
# intervalMeasurementTime:
measurement_job = crontab.new(
    command="python3 /var/wheaterstation/script/wsControl.py")
measurement_job.day.every(yamlconfig["Config"][0]["day"])
config_array.append(yamlconfig["Config"][0]["day"])
measurement_job.hour.every(yamlconfig["Config"][0]["hour"])
config_array.append(yamlconfig["Config"][0]["hour"])
measurement_job.minute.every(yamlconfig["Config"][0]["minute"])
config_array.append(yamlconfig["Config"][0]["minute"])
measurement_job.second.every(yamlconfig["Config"][0]["second"])
config_array.append(yamlconfig["Config"][0]["second"])

# updateInterval
updateInterval_job = crontab.new(
    command="bash /var/wheaterstation/system/updateWS.sh")
measurement_job.day.every(yamlconfig["Config"][1]["day"])
config_array.append(yamlconfig["Config"][1]["day"])
measurement_job.hour.every(yamlconfig["Config"][1]["hour"])
config_array.append(yamlconfig["Config"][1]["hour"])
measurement_job.minute.every(yamlconfig["Config"][1]["minute"])
config_array.append(yamlconfig["Config"][1]["minute"])
measurement_job.second.every(yamlconfig["Config"][1]["second"])
config_array.append(yamlconfig["Config"][1]["second"])

# write into crontab
crontab.write()
logger.info("Config applied")

# Write the config into the database
cursor.execute("""
    insert into measurement (
        intervalMeasurementTime_day,
        intervalMeasurementTime_hour,
        intervalMeasurementTime_minute,
        intervalMeasurementTime_second,
        updateInterval_day,
        updateInterval_hour,
        updateInterval_minute,
        updateInterval_second
        )
    VALUES (?,?,?,?,?,?,?,?)""", config_array)
connection.commit()
connection.close()
