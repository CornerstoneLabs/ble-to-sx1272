# import requests
# requests.post("http://server:1337/beacons/touch", data=data_payload)
import sys
import queue
import send
import blescan
import bluetooth._bluetooth as bluez


def start_scanner():
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
        print("ble thread started")

    except:
        print("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    return sock


def scan_loop(sock):
    while True:
        returned_list = blescan.parse_events(sock, 10)
        print("scanning")
        for beacon in returned_list:
            queue.queue_beacon(beacon)
            # print(beacon)
            # try:
            #     data_payload = {
            #         "mac": beacon.split(',')[0],
            #         "raw": beacon,
            #         "source": SCANNER_ID
            #     }
            #     print(queue.create_key(beacon))
            #     print(data_payload)

            # except Exception, ex:
            #     print ('error')
            #     print ex


if __name__ == "__main__":
    sock = start_scanner()
    scan_loop(sock)
