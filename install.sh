#!/bin/bash

sudo apt-get update 
sudo apt-get install -y libusb-dev 
sudo apt-get install -y libdbus-1-dev 
sudo apt-get install -y libglib2.0-dev --fix-missing
sudo apt-get install -y libudev-dev 
sudo apt-get install -y libical-dev
sudo apt-get install -y libreadline-dev
sudo apt-get install -y libdbus-glib-1-dev
sudo apt-get install -y readline-dev
sudo apt-get install -y python-setuptools
sudo easy_install pip

./install-bluez.sh
./install-crontab.sh

sudo reboot

