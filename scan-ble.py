# test BLE Scanning software
# jcs 6/8/2014

from ..ibeacon_scanner import blescan
import sys
import requests
import os
import bluetooth._bluetooth as bluez

SCANNED_DATA_FILENAME = 'scanned_numbers.txt'
SCANNER_ID='9d3c2169-3be5-4ae6-9be9-2bc2cbd49ccb'

dev_id = 0
try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"

except:
        print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

def read_list():
	if os.path.exists(SCANNED_DATA_FILENAME):
		with open(SCANNED_DATA_FILENAME, 'rt') as read_handle:
			read_buffer = read_handle.read()
		return read_buffer
	return ''

def create_key(item):
	data = item.split(',')
	key = '%s_%s_%s' % (item[1], item[2], item[3])
	return key

while True:
        returnedList = blescan.parse_events(sock, 10)
        print "----------"
        for beacon in returnedList:
                print beacon
                try:
                        data_payload = {
                                "mac": beacon.split(',')[0],
                                "raw": beacon,
                                "source": SCANNER_ID
                        }
						print(create_key(beacon))
                        print(data_payload)
                        requests.post("http://server:1337/beacons/touch", data = data_payload)
                except Exception, ex:
                        print ('error')
                        print ex
