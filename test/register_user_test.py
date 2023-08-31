import random

from utils.api_utils import post_req
from utils.data_utils import generate_string_data


class TestRegisterUser:
    register_endpoint = 'users/register'
    email = f"{generate_string_data(random.randrange(4, 15))}@{generate_string_data(random.randrange(4, 15))}.com"
    name = f"{generate_string_data(random.randrange(4, 15))}"
    password = f"{generate_string_data(random.randrange(6, 15))}"
    invalid_email_string = 'A valid email address is required'
    invalid_name_string = 'User name must be between 4 and 30 characters'
    invalid_password_string = 'Password must be between 6 and 30 characters'
    success_string = 'User account created successfully'
    duplicate_user_string = 'An account already exists with the same email address'

    def test_register_new_user(self):
        payload = {
            "email": self.email,
            "name": self.name,
            "password": self.password
        }

        resp = post_req(self.register_endpoint, payload)
        json_vals = resp.json()

        assert json_vals['success'] is True
        assert json_vals['status'] == 201
        assert json_vals['message'] == self.success_string
        assert json_vals['data']['name'] == self.name
        assert json_vals['data']['email'] == self.email

    def test_register_duplicate_email(self):
        resp = ''
        payload = {
            "email": 'dupe@example.com',
            "name": self.name,
            "password": self.password
        }

        for _ in range(2):
            resp = post_req(self.register_endpoint, payload)

        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 409
        assert json_vals['message'] == self.duplicate_user_string

    def test_register_invalid_email(self):
        email_vals = ['invalid', '.com', 'invalid@', '']
        for email in email_vals:
            payload = {
                "email": email,
                "name": self.name,
                "password": self.password
            }

            resp = post_req(self.register_endpoint, payload)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == self.invalid_email_string

    def test_register_invalid_name(self):
        name_vals = ['', 'abc', generate_string_data(random.randrange(31, 35))]
        for name in name_vals:
            payload = {
                "email": self.email,
                "name": name,
                "password": self.password
            }

            resp = post_req(self.register_endpoint, payload)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == self.invalid_name_string

    def test_register_invalid_password(self):
        password_vals = ['', 'abcde', generate_string_data(random.randrange(31, 35))]
        for password in password_vals:
            payload = {
                "email": self.email,
                "name": self.name,
                "password": password
            }

            resp = post_req(self.register_endpoint, payload)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == self.invalid_password_string
