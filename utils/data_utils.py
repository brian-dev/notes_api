import calendar
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
    with open('yaml_files/endpoints.yml') as file_read:
        file = yaml.safe_load(file_read)
    return file['endpoints']
