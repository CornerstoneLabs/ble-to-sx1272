import os
import json

SCANNED_DATA_FILENAME = 'scanned_numbers.txt'
SCANNER_ID = '9d3c2169-3be5-4ae6-9be9-2bc2cbd49ccb'


def read_list():
    if os.path.exists(SCANNED_DATA_FILENAME):
        with open(SCANNED_DATA_FILENAME, 'rt') as read_handle:
            read_buffer = read_handle.readlines()

        output = []

        if read_buffer != None:
            for item in read_buffer:
                output.append(item.replace('\n', ''))
        return output
    return []


def key_exists(key, list):
    for item in list:
        check_item = item.split('|')[0]
        if check_item == key:
            return True
    return False


def add_key(key):
    with open(SCANNED_DATA_FILENAME, 'at') as write_handle:
        write_handle.write(key + '\n')


def remove_key(key):
    read_buffer = read_list()
    output = []
    for item in read_buffer:
        check_item = item.split('|')[0]
        if check_item == key:
            pass
        else:
            output.append(item + '\n')

    with open(SCANNED_DATA_FILENAME, 'wt') as write_handle:
        write_handle.writelines(output)


def create_key(item):
    data = item.split(',')
    key = '%s_%s_%s' % (data[1], data[2], data[3])
    return key


def is_in_whitelist(item):
    whitelist = [
        '08B209B5-AFEF-4C87-A070-26DDE5F96091'
    ]

    data = item.split(',')
    return True # data[1] in whitelist


def get_location():
    if os.path.exists('gps.txt'):
        with open('gps.txt', 'rt') as read_handle:
            gps_data = read_handle.read()
        parsed_gps_data = json.loads(gps_data)
        return '|lat:%s,lng:%s,t:%s' % (parsed_gps_data['latitude'], parsed_gps_data['longitude'], parsed_gps_data['t'])
    return '|NO_LOCATION'


def queue_beacon(item):
    print(item)
    if is_in_whitelist(item):
        key = create_key(item)

        buffer = read_list()
        if key_exists(key, buffer):
            pass
        else:
            data = get_location()
            add_key(key + data)
