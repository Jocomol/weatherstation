# WIP
from crontab import CronTab
import yaml
import logging
import sqlite3

# Setup
logging.basicConfig(
    filename='/var/log/weatherstation.log', level=logging.DEBUG)
logger = logging.getLogger("Config")
crontab = CronTab(user='root')
connection = sqlite3.connect('/var/weatherstation/data/wheater.db')
cursor = connection.cursor()
config_array = []

# Load configfile
with open("/var/weatherstation/config.yml", 'r') as stream:
    try:
        yamlconfig = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        logger.error("Error occured appling the config " + exc)

# Cronjob
# intervalMeasurementTime:
measurement_job = crontab.new(
    command="python3 /var/weatherstation/scripts/wsControl.py")
measurement_job.day.every(yamlconfig["Config"][0]["day"])
config_array.append(yamlconfig["Config"][0]["day"])
measurement_job.hour.every(yamlconfig["Config"][0]["hour"])
config_array.append(yamlconfig["Config"][0]["hour"])
measurement_job.minute.every(yamlconfig["Config"][0]["minute"])
config_array.append(yamlconfig["Config"][0]["minute"])

# updateInterval
update_job = crontab.new(
    command="bash /var/weatherstation/system/updateWS.sh")
update_job.day.every(yamlconfig["Config"][1]["day"])
config_array.append(yamlconfig["Config"][1]["day"])
update_job.hour.every(yamlconfig["Config"][1]["hour"])
config_array.append(yamlconfig["Config"][1]["hour"])
update_job.minute.every(yamlconfig["Config"][1]["minute"])
config_array.append(yamlconfig["Config"][1]["minute"])

crontab.write()
logger.info("Config applied")

# Write the config into the database
cursor.execute("""
    insert into config (
        intervalMeasurementTime_day,
        intervalMeasurementTime_hour,
        intervalMeasurementTime_minute,
        updateInterval_day,
        updateInterval_hour,
        updateInterval_minute
        )
    VALUES (?,?,?,?,?,?)""", config_array)
connection.commit()
connection.close()
