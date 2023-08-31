import os
import pytest
import yaml

from dotenv import load_dotenv
from utils.api_utils import register_new_user, login_user, delete_user

load_dotenv()

test_user = {
    'name': os.getenv('DEFAULT_NAME'),
    'email': os.getenv('DEFAULT_EMAIL'),
    'password': os.getenv('DEFAULT_PASSWORD')
}


@pytest.fixture(scope='session', autouse=True)
def register():
    register_new_user(test_user)
    with open(f'./yaml/endpoints.yaml') as file_read:
        file = yaml.load(file_read, Loader=yaml.FullLoader)
    return file['endpoints']


@pytest.fixture(scope='session', autouse=True)
def strings():
    with open(f'./yaml/endpoints.yaml') as file_read:
        file = yaml.load(file_read, Loader=yaml.FullLoader)
    return file['endpoints']


@pytest.fixture(scope='session')
def default_user():
    user_creds = {
        'email': test_user['email'],
        'password': test_user['password']
    }

    user_info = login_user(user_creds)
    yield user_info

    delete_user(user_info['data']['token'])
