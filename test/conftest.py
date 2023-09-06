import time
import pytest

from utils.data_utils import generate_user_payload
from utils.system_api import SystemApi
from utils.user_api import UserApi

user_api = UserApi()
sys_api = SystemApi()
test_user = generate_user_payload()
update_user_creds = generate_user_payload()


@pytest.fixture(scope='session', autouse=True)
def register():
    health_status = sys_api.sys_check('health')
    if health_status['status'] == 200:
        user_api.register_new_user('register', test_user)
        time.sleep(1)
        user_api.register_new_user('register', update_user_creds)
    else:
        raise Exception(f"System might be down. System returned {health_status}")


@pytest.fixture(scope='session')
def default_user():
    user_creds = {
        'email': test_user['email'],
        'password': test_user['password']
    }

    user_info = user_api.login_user('login', user_creds)
    yield user_info

    user_api.delete_user('delete', user_info['data']['token'])


@pytest.fixture(scope='session')
def update_user():
    user_creds = {
        'email': update_user_creds['email'],
        'password': update_user_creds['password']
    }

    user_to_update = user_api.login_user('login', user_creds)
    yield user_to_update

    user_api.delete_user('delete', user_to_update['data']['token'])
