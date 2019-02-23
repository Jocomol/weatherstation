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
# time_measureInterval:
time_measurement-job = crontab.new(
    command="python3 /var/weatherstation/scripts/wsControl.py")
time_measurement-job.dow.on(yamlconfig["Config"][0]["weekday"])
time_measurement-job.month.during(yamlconfig["Config"][0]["month"])
time_measurement-job.day.every(yamlconfig["Config"][0]["day"])
time_measurement-job.hour.every(yamlconfig["Config"][0]["hour"])
time_measurement-job.minute.every(yamlconfig["Config"][0]["minute"])
config_array.append(yamlconfig["Config"][0]["weekday"])
config_array.append(yamlconfig["Config"][0]["month"])
config_array.append(yamlconfig["Config"][0]["day"])
config_array.append(yamlconfig["Config"][0]["hour"])
config_array.append(yamlconfig["Config"][0]["minute"])

# updateInterval
time_update-job = crontab.new(
    command="bash /var/weatherstation/system/updateWS.sh")
time_update-job.dow.on(yamlconfig["Config"][0]["weekday"])
time_update-job.month.during(yamlconfig["Config"][0]["month"])
time_update-job.day.every(yamlconfig["Config"][0]["day"])
time_update-job.hour.every(yamlconfig["Config"][0]["hour"])
time_update-job.minute.every(yamlconfig["Config"][0]["minute"])
config_array.append(yamlconfig["Config"][1]["weekday"])
config_array.append(yamlconfig["Config"][1]["month"])
config_array.append(yamlconfig["Config"][1]["day"])
config_array.append(yamlconfig["Config"][1]["hour"])
config_array.append(yamlconfig["Config"][1]["minute"])

crontab.write()
logger.info("Config applied")

# Write the config into the database
cursor.execute("""
    insert into config (
        time_measureInterval_weekday,
        time_measureInterval_month,
        time_measureInterval_day,
        time_measureInterval_hour,
        time_measureInterval_minute,
        time_updateInterval_weekday,
        time_updateInterval_month,
        time_updateInterval_day,
        time_updateInterval_hour,
        time_updateInterval_minute
        )
    VALUES (?,?,?,?,?,?,?,?,?,?)""", config_array)
connection.commit()
connection.close()
