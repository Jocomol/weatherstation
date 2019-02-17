#!/bin/bash
##################################
#Author: Joe Meier a.k.a Jocomol #
#Contact: joelmeier08@gmail.com  #
##################################

#Check if sudo
if [ "$EUID" -ne 0 ];
then
        echo "Please run as root"
	exit
fi

#raspi-config

#install software
echo "Installing required software"
##TESTING
echo "No software installed because of Testing"
#apt update
#apt install python3 python3-pip tree openssh-server sqlite3 apache2 php7.2 php7.2-sqlite3 figlet -y &> /dev/null
##
echo "Software installed"

#making file structure
mkdir /var/wheaterstation
mkdir /var/wheaterstation/data
mkdir /var/wheaterstation/scripts
mkdir /var/wheaterstation/hardware
mkdir /var/wheaterstation/frontend
mkdir /var/wheaterstation/log
ln -s /sys/bus/w1/devices/28-000005d2e508 /var/wheaterstation/hardware/ds1820 #Thermometer
ln -s /var/www/html /var/wheaterstation/frontend
touch /var/wheaterstation/data/wheater.db
touch /var/log/wheaterstation.log
ln -s /var/log/ /var/wheaterstation/log

#move additonal files
cp files/motd/* /etc/update-motd.d/ &> /dev/null

#configuring hardware
#ds1820
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


#configuring software
#Database
sqlite3 /var/wheaterstation/data/wheater.db < install_script/createDB.sql

#scrLib
pip3 install pytemperature
cp scrLib/wsControl.py /var/wheaterstation/scripts
cp scrLib/thermo.py /var/wheaterstation/scripts
cp scrLib/dbConnector.py /var/wheaterstation/scripts
cp scrLib/logger.py /var/wheaterstation/scripts
cp scrLib/wsPart.py /var/wheaterstation/scripts

#making ssh keys
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

#cleanup

#restart
echo "Now Restarting"
if  [ $# -ge 1 ] && [ "$1" == "-t" ];
then
        echo "[Testing] SCRIPT DONE"
else
        init 6
fi
