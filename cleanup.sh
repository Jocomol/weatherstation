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

rm -r /var/wheaterstation &> /dev/null
rm -r /tmp/installFiles &> /dev/null

echo "Cleaned"

