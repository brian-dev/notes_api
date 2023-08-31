import random

from utils.api_utils import post_req
from utils.data_utils import generate_string_data


class TestLoginUser:
    login_endpoint = 'users/login'
    email = f"{generate_string_data(random.randrange(4, 15))}@{generate_string_data(random.randrange(4, 15))}.com"
    password = f"{generate_string_data(random.randrange(6, 15))}"
    invalid_email_string = 'A valid email address is required'
    invalid_password_string = 'Password must be between 6 and 30 characters'
    incorrect_password_string = 'Incorrect email address or password'

    def test_user_login(self, login):
        assert login['success'] is True
        assert login['status'] == 200
        assert login['message'] == 'Login successful'
        assert login['data']['name'] == 'tester'
        assert login['data']['email'] == 'a@example.com'

    def test_invalid_email(self):
        email_vals = ['', 'invalid', 'test@', 'test.com']
        for email in email_vals:
            payload = {
                "email": email,
                "password": self.password
            }

            resp = post_req(self.login_endpoint, payload)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == self.invalid_email_string

    def test_invalid_password(self):
        password_vals = ['', 'abcde', generate_string_data(random.randrange(31, 35))]
        for password in password_vals:
            payload = {
                "email": self.email,
                "password": password
            }

            resp = post_req(self.login_endpoint, payload)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == self.invalid_password_string

    def test_incorrect_password(self):
        payload = {
            "email": self.email,
            "password": 'incorrectPassword'
        }

        resp = post_req(self.login_endpoint, payload)
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == self.incorrect_password_string
