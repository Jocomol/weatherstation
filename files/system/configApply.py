from crontab import CronTab
import yaml
import logging
import sqlite3

# Setup
try:
    logging.basicConfig(
        filename='/var/log/weatherstation.log', level=logging.DEBUG)
    logger = logging.getLogger("Config")
    crontab = CronTab(user='root')
    connection = sqlite3.connect('/var/weatherstation/data/weather.db')
    cursor = connection.cursor()
    config_array = []
    yaml.warnings({'YAMLLoadWarning': False})
except OSError:
    print(colorful.red("Root priviledges needed for this command."))
    print(colorful.red("Please execute: "))
    print(colorful.italic("sudo wsmanage configapply"))
    logger.error("User tried opening cron tab without root priviledges")


# Load configfile
with open("/var/weatherstation/config.yml", 'r') as stream:
    try:
        yamlconfig = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(colorful.bold_red(exc))
        logger.error("Error occured appling the config " + exc)

try:
    # Cronjob
    # time_measureInterval:
    time_measurement_job = crontab.new(
        command="python3 /var/weatherstation/scripts/wsControl.py")
    if yamlconfig["Config"][0]["weekday"] is not None:
        time_measurement_job.dow.on(yamlconfig["Config"][0]["weekday"])
    if yamlconfig["Config"][0]["month"] is not None:
        time_measurement_job.month.during(yamlconfig["Config"][0]["month"])
    if yamlconfig["Config"][0]["day"] is not None:
        time_measurement_job.day.every(yamlconfig["Config"][0]["day"])
    if yamlconfig["Config"][0]["hour"] is not None:
        time_measurement_job.hour.every(yamlconfig["Config"][0]["hour"])
    if yamlconfig["Config"][0]["minute"] is not None:
        time_measurement_job.minute.every(yamlconfig["Config"][0]["minute"])

    # updateInterval
    time_update_job = crontab.new(
        command="bash /var/weatherstation/system/updateWS.sh")
    if yamlconfig["Config"][1]["weekday"] is not None:
        time_update_job.dow.on(yamlconfig["Config"][1]["weekday"])
    if yamlconfig["Config"][1]["month"] is not None:
        time_update_job.month.during(yamlconfig["Config"][1]["month"])
    if yamlconfig["Config"][1]["day"] is not None:
        time_update_job.day.every(yamlconfig["Config"][1]["day"])
    if yamlconfig["Config"][1]["hour"] is not None:
        time_update_job.hour.every(yamlconfig["Config"][1]["hour"])
    if yamlconfig["Config"][1]["minute"] is not None:
        time_update_job.minute.every(yamlconfig["Config"][1]["minute"])
except IOError:
    print(colorful.bold_red("""Not enough priviledges to change cronjobs.
            please start wsmanage configapply again with root privileges"""))

config_array.append(yamlconfig["Config"][0]["weekday"])
config_array.append(yamlconfig["Config"][0]["month"])
config_array.append(yamlconfig["Config"][0]["day"])
config_array.append(yamlconfig["Config"][0]["hour"])
config_array.append(yamlconfig["Config"][0]["minute"])
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
