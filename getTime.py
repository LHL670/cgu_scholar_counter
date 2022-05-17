import datetime


def currentTime():
    now = datetime.datetime.now()
    currentTime = now.strftime("%Y-%m-%d")
    return currentTime
