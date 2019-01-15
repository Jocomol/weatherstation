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
apt update
apt install tree openssh-server sqlite3 apache2 php7.2 php7.2-sqlite3 figlet -y &> /dev/null
echo "Software installed"

#making file structure
mkdir /var/wheaterstation
mkdir /var/wheaterstation/data
mkdir /var/wheaterstation/scripts
mkdir /var/wheaterstation/hardware
ln -s /sys/bus/w1/devices/28-000005d2e508 /var/wheaterstation/hardware/ds1820
ln -s /var/www/html /var/wheaterstation/frontend
touch /var/wheaterstation/data/wheaterdb.db

#configuring hardware
#ds1820
lsmod
modprobe wire
modprobe w1-gpio
modporbe w1-therm
echo "wire" >> /etc/modules
echo "w1-gpio" >> /etc/modules
echo "w1-therm" >> /etc/modules
echo "#1-Wire ds1820" >> /boot/config.txt
echo "dtoverlay=w1-gpio" >> /boot/config.txt
echo "gpiopin=4" >> /boot/config.txt


#configuring software
sqlite3 /var/wheaterstation/data/wheater.db < install_script/createDB.sql

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

if [ $# == 1 ] && [ "$1" == "-t" ];
then
        echo "[Testing] NOT DELETING CONFIG"
else
        rm config
fi

#restart
echo "Now Restarting"
if  [ $# == 1 ] && [ "$1" == "-t" ];
then
        echo "[Testing] SCRIPT DONE"
else
        init 6
fi


