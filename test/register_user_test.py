import random

import allure

from utils.data_utils import generate_string_data
from utils.user_api import UserApi


class TestRegisterUser(UserApi):
    email = f"{generate_string_data(random.randrange(4, 15))}@{generate_string_data(random.randrange(4, 15))}.com"
    name = f"{generate_string_data(random.randrange(4, 15))}"
    password = f"{generate_string_data(random.randrange(6, 15))}"
    invalid_email_string = 'A valid email address is required'
    invalid_name_string = 'User name must be between 4 and 30 characters'
    invalid_password_string = 'Password must be between 6 and 30 characters'
    success_string = 'User account created successfully'
    duplicate_user_string = 'An account already exists with the same email address'

    @allure.feature('register_user')
    def test_register_new_user(self):
        payload = {
            "email": self.email,
            "name": self.name,
            "password": self.password
        }

        resp = self.register_new_user('register', payload)

        assert resp['success'] is True
        assert resp['status'] == 201
        assert resp['message'] == self.success_string
        assert resp['data']['name'] == self.name
        assert resp['data']['email'] == self.email

    @allure.feature('register_user')
    def test_register_duplicate_email(self):
        payload = {
            "email": 'dupe@example.com',
            "name": self.name,
            "password": self.password
        }

        for _ in range(2):
            resp = self.register_new_user('register', payload)

        assert resp['success'] is False
        assert resp['status'] == 409
        assert resp['message'] == self.duplicate_user_string

    @allure.feature('register_user')
    def test_register_invalid_email(self):
        email_vals = ['invalid', '.com', 'invalid@', '']
        for email in email_vals:
            payload = {
                "email": email,
                "name": self.name,
                "password": self.password
            }

            resp = self.register_new_user('register', payload)

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == self.invalid_email_string

    @allure.feature('register_user')
    def test_register_invalid_name(self):
        name_vals = ['', 'abc', generate_string_data(random.randrange(31, 35))]
        for name in name_vals:
            payload = {
                "email": self.email,
                "name": name,
                "password": self.password
            }

            resp = self.register_new_user('register', payload)

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == self.invalid_name_string

    @allure.feature('register_user')
    def test_register_invalid_password(self):
        password_vals = ['', 'abcde', generate_string_data(random.randrange(31, 35))]
        for password in password_vals:
            payload = {
                "email": self.email,
                "name": self.name,
                "password": password
            }

            resp = self.register_new_user('register', payload)

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == self.invalid_password_string
