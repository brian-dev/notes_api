import os
import sys
import time
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from python_api.utils.data_utils import generate_user_payload
import python_api.utils.system_api
import python_api.utils.user_api
from core_framework.core import Core

user_api = python_api.utils.user_api.UserApi()
sys_api = python_api.utils.system_api.SystemApi()
base_api = Core().initialize_core()
test_user = generate_user_payload()
update_user_creds = generate_user_payload()


@pytest.fixture(scope='session', autouse=True)
def register():
    health_status = sys_api.sys_check('health', base_api)
    if health_status['status'] == 200:
        user_api.register_new_user('register', test_user, base_api)
        time.sleep(1)
        user_api.register_new_user('register', update_user_creds, base_api)
    else:
        raise Exception(f"System might be down. System returned {health_status}")


@pytest.fixture(scope='session')
def default_user():
    user_creds = {
        'email': test_user['email'],
        'password': test_user['password']
    }

    user_info = user_api.login_user('login', user_creds, base_api)
    yield user_info

    user_api.delete_user('delete', user_info['data']['token'], base_api)


@pytest.fixture(scope='session')
def update_user():
    user_creds = {
        'email': update_user_creds['email'],
        'password': update_user_creds['password']
    }

    user_to_update = user_api.login_user('login', user_creds, base_api)
    yield user_to_update

    user_api.delete_user('delete', user_to_update['data']['token'], base_api)
