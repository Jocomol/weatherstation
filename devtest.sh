#!/bin/bash
##################################
#Author: Joe Meier a.k.a Jocomol #
#Contact: joelmeier08@gmail.com  #
##################################
echo "This Script is for development only"
#Check if sudo
if [ "$EUID" -ne 0 ];
then
        echo "Please run as root"
	exit
fi

bash development/cleanup.sh
bash install.sh -t
python3 /var/weatherstation/system/configApply.py
python3 /var/weatherstation/scripts/wsControl.py
echo "Done"
