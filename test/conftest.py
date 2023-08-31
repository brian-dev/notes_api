import pytest
import requests

from utils.api_utils import base_url, auth_headers, register_new_user, login_user, delete_user

test_user = {
    'name': 'tester',
    'email': 'a@example.com',
    'password': 'password'
}


@pytest.fixture(scope='session', autouse=True)
def register():
    register_new_user(test_user)


@pytest.fixture(scope='session')
def login():
    user_creds = {
        'email': test_user['email'],
        'password': test_user['password']
    }

    user = login_user(user_creds)
    yield user

    delete_user(user['data']['token'])
