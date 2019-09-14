#!/usr/bin/env bash

apt update
apt upgrade -y
apt dist-upgrade -y
apt autoremove -y 
pip3 install pytemperature python-crontab pyyaml
