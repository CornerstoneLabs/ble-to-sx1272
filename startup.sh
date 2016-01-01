#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

sudo hciconfig hci0 up
export SCANNER_ID="3a48542a-77b8-41f9-99b1-92d943829ccd"
sudo python scanble.py
