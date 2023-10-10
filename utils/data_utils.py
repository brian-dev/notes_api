import calendar
import os
import random
import string
import time
import yaml


def generate_timestamp():
    return str(calendar.timegm(time.gmtime()))


def generate_string_data(length):
    return str(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))


def generate_number_data(length):
    return str(''.join(random.choices(string.digits, k=length)))


def generate_user_payload():
    name = generate_string_data(random.randrange(4, 15))
    email = generate_string_data(random.randrange(4, 15))
    payload = {
        'name': name,
        'email': f"{email}@example.com",
        'password': 'password'
    }

    return payload


def fetch_endpoints():
    file_dir = __file__
    parent_dir = os.path.split(file_dir)[0]
    top_level_dir = os.path.split(parent_dir)[0]
    with open(f"{top_level_dir}/yaml_files/endpoints.yaml") as file_read:
        file = yaml.safe_load(file_read)
    return file['endpoints']
