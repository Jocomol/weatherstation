#!/bin/bash
##################################
#Author: Joe Meier a.k.a Jocomol #
#Contact: joelmeier08@gmail.com  #
##################################

#Check if sudo

#raspi-config

#install software
apt-get install git tree openssh-server sqlite3 apache2 php7.0 php7.0-sqlite3 figlet -y

#git pull für scripts

#configuring software
	#execute SQL scripts
	#network config

#making ssh keys
if [ ! -f /home/pi/.ssh/authorized_keys ]; then
	mkdir /home/pi/.ssh
	chmod 700 /home/pi/.ssh
	cd /home/pi/.ssh
	touch authorized_keys
	chmod 600 authorized_keys
	ssh-keygen -f '/home/pi/.ssh/id_rsa' -N ''
	cat home/pi/.ssh/id_rsa.pub >> /home/pi/.ssh/authorized_keys
fi

#restart
if  [ $# == 1 ] && [ "$1" == "-t" ]; 
then 
        echo "SCRIPT DONE"; 
else 
        init 6
fi

