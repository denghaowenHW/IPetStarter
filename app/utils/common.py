import datetime


def get_current_time():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now_time

