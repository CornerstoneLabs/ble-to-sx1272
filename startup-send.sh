#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

sleep 5
export SCANNER_ID="3a48542a-77b8-41f9-99b1-92d943829ccd"
sudo python send.py >> /home/pi/send_log.txt
