import subprocess

def disk_space():
    process = subprocess.Popen(["df"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    device, size, used, available, percent, mountpoint = output.split("\n")[1].split()
    return device, size, used, available, percent, mountpoint

