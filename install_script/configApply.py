##WIP
import yaml
from crontab import CronTab
##intervalMeasurementTime:
with open("../config.yml", 'r') as stream:
    try:
        yamlconfig = yaml.dump(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)

print(yamlconfig["Config"]["intervalMeasurementTime"]["minutes"])
##intervalMeasurementTime:


##Cronjob
crontab = CronTab()
