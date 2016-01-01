#!/bin/bash
cd /home/pi/Documents/ble-to-sx1272
sudo hciconfig hci0 up

export SCANNER_ID="3a48542a-77b8-41f9-99b1-92d943829ccd"
sudo python scanble.py
