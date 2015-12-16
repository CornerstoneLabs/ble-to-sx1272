import datetime

MAX_SECONDS = 60
LAST_RUN = None


def set_last_run():
    global LAST_RUN
    LAST_RUN = datetime.datetime.now()


def initialise():
    set_last_run()


def time_difference():
    global LAST_RUN
    delta = datetime.datetime.now() - LAST_RUN

    return delta.seconds


def check_keepalive():
    if time_difference() > MAX_SECONDS:
        set_last_run()

        return("%s" % datetime.datetime.now())
    else:
        return None
