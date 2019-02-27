#!/bin/bash
##################################
#Author: Joe Meier a.k.a Jocomol #
#Contact: joelmeier08@gmail.com  #
##################################

##Check if sudo
if [ "$EUID" -ne 0 ];
then
        echo "Please run as root"
	exit
fi

##raspi-config

##install software
echo "Installing required software"
##TESTING
echo "No software installed because of Testing"
#apt update
#apt install python3 python3-pip tree openssh-server sqlite3 apache2 php7.2 php7.2-sqlite3 figlet -y &> /dev/null
##
echo "Software installed"

if  [ "$1" == "-t" ];
then
  mkdir /tmp/tempweatherstation
  cp /var/weatherstation/data/weather.db  /tmp/tempweatherstation &> /dev/null
  cp /var/weatherstation/config.yml  /tmp/tempweatherstation &> /dev/null
fi

## Delete old files
rm -r /var/weatherstation

##making file structure
mkdir /var/weatherstation
mkdir /var/weatherstation/data
mkdir /var/weatherstation/scripts
mkdir /var/weatherstation/hardware
mkdir /var/weatherstation/frontend
mkdir /var/weatherstation/log
mkdir /var/weatherstation/system
ln -s /sys/bus/w1/devices/28-000005d2e508 /var/weatherstation/hardware/ds1820 #Thermometer
ln -s /var/www/html /var/weatherstation/frontend
if  [ "$1" != "-t" ];
then
  touch /var/weatherstation/data/weather.db
fi
rm /var/log/weatherstation.log &> /dev/null
touch /var/log/weatherstation.log
chmod 777 /var/log/weatherstation.log
ln -s /var/log/ /var/weatherstation/log

##configuring hardware
##ds1820 (Thermometer)
lsmod
modprobe wire
modprobe w1-gpio
modprobe w1-therm
echo "wire" >> /etc/modules
echo "w1-gpio" >> /etc/modules
echo "w1-therm" >> /etc/modules
echo "#1-Wire ds1820" >> /boot/config.txt
echo "dtoverlay=w1-gpio" >> /boot/config.txt
echo "gpiopin=4" >> /boot/config.txt

##configuring software
##Database
if  [ "$1" != "-t" ];
then
        sqlite3 /var/weatherstation/data/weather.db < install_script/createDB.sql
fi

##scrLib
pip3 install -r requirements.txt
cp scrLib/wsControl.py /var/weatherstation/scripts
cp scrLib/thermo.py /var/weatherstation/scripts
cp scrLib/dbConnector.py /var/weatherstation/scripts
cp scrLib/wsPart.py /var/weatherstation/scripts

##making ssh keys
echo "Making ssh keys"
if [ ! -f /home/pi/.ssh/authorized_keys ]; then
	mkdir /home/pi/.ssh
	chmod 700 /home/pi/.ssh
	cd /home/pi/.ssh
	touch authorized_keys
	chmod 600 authorized_keys
	ssh-keygen -f '/home/pi/.ssh/id_rsa' -N '' &> /dev/null
	cat home/pi/.ssh/id_rsa.pub >> /home/pi/.ssh/authorized_keys
fi
echo "The ssh keys are stored in /home/pi/.ssh"

##system
if  [ "$1" == "-t" ];
then
  cp /tmp/tempweatherstation/weather.db /var/weatherstation/data/
  cp /tmp/tempweatherstation/config.yml /var/weatherstation/
else
  cp config.yml /var/weatherstation
fi
cp files/motd/* /etc/update-motd.d/ &> /dev/null
cp files/system/configApply.py /var/weatherstation/system
cp files/system/updateWS.sh /var/weatherstation/system
cp files/system/showconfig.py /var/weatherstation/system
chmod -R 777 /var/weatherstation/
python3 /var/weatherstation/system/configApply.py
cp files/system/wsmanage.sh /usr/bin/wsmanage
chmod 777 /usr/bin/wsmanage

##cleanup
crontab -r

##restart
echo "Now Restarting"
if  [ $# -ge 1 ] && [ "$1" == "-t" ];
then
        echo "[Testing] SCRIPT DONE"
else
        init 6
fi
