import os
import pytest
import yaml

from dotenv import load_dotenv
from utils.user_api import UserApi

load_dotenv()

user_api = UserApi()

test_user = {
    'name': os.getenv('DEFAULT_NAME'),
    'email': os.getenv('DEFAULT_EMAIL'),
    'password': os.getenv('DEFAULT_PASSWORD')
}


@pytest.fixture(scope='session', autouse=True)
def register():
    user_api.register_new_user(test_user)


@pytest.fixture(scope='session')
def default_user():
    user_creds = {
        'email': test_user['email'],
        'password': test_user['password']
    }

    user_info = user_api.login_user(user_creds)
    yield user_info

    user_api.delete_user(user_info['data']['token'])
