from utils.api_utils import get_req


class TestUserProfile:
    profile_endpoint = 'users/profile'

    def test_get_user_profile(self, login):
        resp = get_req(self.profile_endpoint, login['data']['token'])
        json_vals = resp.json()

        assert json_vals['success'] is True
        assert json_vals['status'] == 200
        assert json_vals['message'] == 'Profile successful'
        assert json_vals['data']['name'] == 'tester'
        assert json_vals['data']['email'] == 'a@example.com'

    def test_empty_auth_token(self, login):
        resp = get_req(self.profile_endpoint, '')
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == 'No authentication token specified in x-auth-token header'

    def test_invalid_auth_token(self, login):
        resp = get_req(self.profile_endpoint, 'invalidToken')
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == 'Access token is not valid or has expired, you will need to login'
