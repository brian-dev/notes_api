from utils.base_api import BaseApi
from utils.data_utils import fetch_endpoints


class TestUserProfile(BaseApi):
    endpoints = fetch_endpoints()

    def test_get_user_profile(self, default_user):
        resp = self.get_req(self.endpoints['profile'], default_user['data']['token'])
        json_vals = resp.json()

        assert json_vals['success'] is True
        assert json_vals['status'] == 200
        assert json_vals['message'] == 'Profile successful'
        assert json_vals['data']['name'] == 'tester'
        assert json_vals['data']['email'] == 'a@example.com'

    def test_empty_auth_token(self):
        resp = self.get_req(self.endpoints['profile'], '')
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == 'No authentication token specified in x-auth-token header'

    def test_invalid_auth_token(self):
        resp = self.get_req(self.endpoints['profile'], 'invalidToken')
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == 'Access token is not valid or has expired, you will need to login'
