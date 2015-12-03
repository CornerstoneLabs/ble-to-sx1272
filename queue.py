import os

SCANNED_DATA_FILENAME = 'scanned_numbers.txt'
SCANNER_ID = '9d3c2169-3be5-4ae6-9be9-2bc2cbd49ccb'


def read_list():
    if os.path.exists(SCANNED_DATA_FILENAME):
        with open(SCANNED_DATA_FILENAME, 'rt') as read_handle:
            read_buffer = read_handle.readlines()

        output = []
        for item in read_buffer:
            output.append(item.replace('\n', ''))
        return output
    return []


def key_exists(key, list):
    for item in list:
        if item == key:
            return True
    return False


def add_key(key):
    with open(SCANNED_DATA_FILENAME, 'at') as write_handle:
        write_handle.write(key + '\n')


def remove_key(key):
    read_buffer = read_list()
    output = []
    for item in read_buffer:
        if item == key:
            pass
        else:
            output.append(item + '\n')

    with open(SCANNED_DATA_FILENAME, 'wt') as write_handle:
        write_handle.writelines(output)


def create_key(item):
    data = item.split(',')
    key = '%s_%s_%s' % (data[1], data[2], data[3])
    return key


def queue_beacon(item):
    key = create_key(item)

    buffer = read_list()
    if key_exists(key, buffer):
        pass
    else:
        add_key(key)
