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

rm -r /var/weatherstation &> /dev/null
rm /var/log/weatherstation.log  &> /dev/null
echo "Cleaned"
