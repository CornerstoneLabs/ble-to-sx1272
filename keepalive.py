import datetime

MAX_SECONDS = 60


def set_last_run():
    global last_run
    last_run = datetime.datetime.now()


def initialise():
    set_last_run()


def time_difference():
    global last_run
    delta = datetime.datetime.now() - last_run

    return delta.seconds


def check_keepalive():
    if time_difference() > MAX_SECONDS:
        set_last_run()

        return True
    else:
        return False
