#!/bin/bash
import subprocess
import queue
from subprocess import Popen

def log(message):
    handle = open('boop.log', 'at')
    handle.write('%s\n' % message);
    handle.close()


def format_message(message):
    message = ('"%s"' % message)
    return message


def generate_command(address, message):
    return './boop %s %s' % (str(address), message)


def send(address, message):
    message = format_message(message)
    command_string = generate_command(address, message)
    print command_string
    return_buffer = Popen(
        command_string,
        shell=True, stdout=subprocess.PIPE
    ).stdout.read()
    log(return_buffer)


def time_sends():
    import uuid
    import time

    iterations = 100
    start = time.time()
    for a in range(iterations):
        send(1, uuid.uuid4())
    end = time.time()
    print('%s messages in %s seconds' % (iterations, end - start))


def send_keys():
    items = queue.read_list()
    if len(items) > 0:
        send_key = items[0]

        try:
            send(1, send_key)
        except Exception, ex:
            send(1, "Invalid key. %s" % ex)

        queue.remove_key(send_key)


if __name__ == "__main__":
    send(1, "Starting send process")

    while True:
        send_keys()
