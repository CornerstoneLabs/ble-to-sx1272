# import requests
# requests.post("http://server:1337/beacons/touch", data=data_payload)
import sys
import queue
import send
import blescan
import bluetooth._bluetooth as bluez
import keepalive
import diagnostics

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

        if len(returned_list) > 0:
            keepalive.set_last_run()

            for beacon in returned_list:
                queue.queue_beacon(beacon)

        if keepalive.check_keepalive():
            send.send(1, "Keepalive")


if __name__ == "__main__":
    send.send(1, "Starting BLE watcher")

    device, size, used, available, percent, mountpoint = diagnostics.disk_space()
    send.send(1, "m:%s a:%s s:%s p:%s" % (mountpoint, available, size, percent))

    keepalive.initialise()

    sock = start_scanner()
    scan_loop(sock)
