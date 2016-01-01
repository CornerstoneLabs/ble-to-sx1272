#!/bin/bash
sudo rm -rf ./bluez
sudo mkdir bluez
cd bluez
sudo wget www.kernel.org/pub/linux/bluetooth/bluez-5.19.tar.gz
sudo gunzip bluez-5.19.tar.gz
sudo tar xvf bluez-5.19.tar
cd bluez-5.19
sudo ./configure --disable-systemd
sudo make
sudo make install

sudo apt-get install -y python-bluez
