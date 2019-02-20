##WIP
import yaml
from crontab import CronTab
##intervalMeasurementTime:
with open("../config.yml", 'r') as stream:
    try:
        yamlconfig = yaml.load(stream))
    except yaml.YAMLError as exc:

##intervalMeasurementTime:


##Cronjob
crontab = CronTab()
