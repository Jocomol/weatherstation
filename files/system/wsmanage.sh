#!/usr/bin/env bash
if [ $# -ge 1 ]
then
  if [ $1 == 'configapply' ]
  then
    python3 /var/weatherstation/system/configApply.py
  elif [ $1 == 'help' ] || [ $1 == "?" ]
  then
    echo "Weatherstation Help"
    echo "-----------------------------------------------------------------------------------------------------"
    echo "| wsmanage configapply                      | Apply the config in /var/weatherstation/config.yml.   |"
    echo "| wsmanage help                             | Show this help.                                       |"
    echo "| wsmanage ?                                | Shows this help.                                      |"
    echo "| wsmanage showconfig                       | Shows the current applied config.                     |"
    echo "| wsmanage measure                          | Executes a measurement.                               |"
    echo "-----------------------------------------------------------------------------------------------------"
    echo "| For more info visit https://github.com/Jocomol/weatherstation                                     |"
    echo "-----------------------------------------------------------------------------------------------------"
  elif [ $1 == 'showconfig' ]
  then
    python3 /var/weatherstation/system/shwoconfig.py
  elif [ $1 == 'measure' ]
  then
    if [ "$EUID" -ne 0 ];
    then
      echo "The force-measure needs root access."
      exit
    else
      python3 /var/weatherstation/scrLib/wsControl.py
    fi
  fi
fi
