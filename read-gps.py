import json
import serial
import pynmea2
import time

serial_handle = serial.Serial('/dev/ttyUSB0',baudrate=4800,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)

run = True
start_time = 0

while run:
    buffer = ''
    try:
        buffer = serial_handle.readline()
    except:
        pass

    if buffer != '':
        try:
            gps_message = None
            gps_message = pynmea2.parse(buffer)

        except:
            pass
    
        if gps_message and gps_message.sentence_type == 'GGA':
            serialize = {
                't': time.time()
            }
            serialize_keys = [ 
                'latitude', 
                'longitude' 
            ]

            for key in serialize_keys:    
                if hasattr(gps_message, key):
                    a = getattr(gps_message, key)
                    serialize[key] = a

            if time.time() > start_time + 60:
                with open('gps.txt', 'wt') as output_handle:
                    output_line = '%s\n' % json.dumps(serialize)
                    output_handle.write(output_line)

                with open('gps_log.txt', 'at') as output_handle:
                    output_line = '%s\n' % json.dumps(serialize)
                    output_handle.write(output_line)

                start_time = time.time()

serial_handle.close()
