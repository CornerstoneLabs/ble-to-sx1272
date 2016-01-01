#!/usr/bin/env python
import subprocess
from subprocess import Popen

command_string = "ps -ax | grep '[0-9] \.\/boop'"

return_buffer = Popen(
    command_string,
    shell=True, stdout=subprocess.PIPE
).stdout.read()
data = return_buffer.split()
print(data)

process_id = data[0]
process_time = data[3]

minutes = int(process_time.split(':')[0])

if minutes > 5:
    Popen("sudo kill -9 " + process_id, shell=True, stdout=subprocess.PIPE).stdout.read()

