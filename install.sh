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
apt-get install git tree openssh-server sqlite3 apache2 php7.0 php7.0-sqlite3 figlet -y &> /dev/null
echo "Software installed"

#git pull für scripts
mkdir /tmp/installFiles
cd /tmp/installFiles
git clone https://github.com/Jocomol/wheaterstation-install.git &> /dev/null

#configuring software
	#execute SQL scripts
	#network config

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
rm -r /tmp/installFiles

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

