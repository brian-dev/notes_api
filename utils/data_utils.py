import calendar
import random
import string
import time


def generate_timestamp():
    return str(calendar.timegm(time.gmtime()))


def generate_string_data(length):
    return str(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
