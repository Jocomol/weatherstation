# WIP
from crontab import CronTab
import yaml

with open("/var/wheaterstation/config.yml", 'r') as stream:
    try:
        yamlconfig = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print(yamlconfig["Config"]["intervalMeasurementTime"]["minutes"])
# intervalMeasurementTime:

#Cronjob
crontab = CronTab()
