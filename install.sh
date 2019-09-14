#!/bin/bash
##################################
#Author: Joe Meier a.k.a Jocomol #
#Contact: joelmeier08@gmail.com  #
##################################

##Check if sudo
if [ "$EUID" -ne 0 ];
then
  echo "[ERROR] Please run as root"
  exit
fi

##TODO raspi-config

echo "[INFO] Installing required software"
if  [ "$1" == "-t" ];
then
  echo "[WARNING] No software installed because of Testing"
else
  apt update
  apt dist-upgrade
  #scrLib
  apt install python3 python3-pip -y
  #data
  apt install sqlite3 -y
  # Web
  apt install apache2 -y
  #system
  apt install tree figlet -y
  echo "Software installed"
fi

if  [ "$1" == "-t" ];
then
  mkdir /tmp/tempweatherstation
  cp /var/weatherstation/data/weather.db  /tmp/tempweatherstation
  cp /var/weatherstation/config.yml  /tmp/tempweatherstation
fi

## SSH
service ssh start
systemctl enable ssh
ssh-add keys/joes_public_key

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
ln -s /sys/bus/w1/devices /var/weatherstation/hardware #Thermometer
ln -s /var/www/html /var/weatherstation/frontend
if  [ "$1" != "-t" ];
then
  touch /var/weatherstation/data/weather.db
fi
rm /var/log/weatherstation.log
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
echo "dtoverlay=w1-gpio,gpiopin=4" >> /boot/config.txt

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

##system
if  [ "$1" == "-t" ] && [ -f /tmp/tempweatherstation/config.yml ];
then
  cp /tmp/tempweatherstation/weather.db /var/weatherstation/data/
  cp /tmp/tempweatherstation/config.yml /var/weatherstation/
else
  cp config.yml /var/weatherstation
fi
cp files/motd/* /etc/update-motd.d/
cp files/system/configApply.py /var/weatherstation/system
cp files/system/updateWS.sh /var/weatherstation/system
cp files/system/showconfig.py /var/weatherstation/system
chmod -R 777 /var/weatherstation/
python3 /var/weatherstation/system/configApply.py
cp files/system/wsmanage.sh /usr/bin/wsmanage
chmod 777 /usr/bin/wsmanage
echo "weatherstation" > /etc/hostname

##cleanup
crontab -r

##restart
echo "[INFO] Now Restarting"
if  [ $# -ge 1 ] && [ "$1" == "-t" ];
then
  echo "[Testing] SCRIPT DONE"
else
  init 6
fi
