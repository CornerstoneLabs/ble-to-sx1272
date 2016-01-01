#!/bin/bash
(crontab -l 2>/dev/null; echo "@reboot $(pwd)/startup.sh") | crontab -
(crontab -l 2>/dev/null; echo "@reboot $(pwd)/startup-send.sh") | crontab -
(crontab -l 2>/dev/null; echo "*/5 * * * * $(pwd)/kill-boop.sh") | crontab -

