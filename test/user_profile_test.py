from utils.user_api import UserApi


class TestUserProfile(UserApi):
    def test_get_user_profile(self, default_user):
        resp = self.get_user_profile('profile', default_user['data']['token'])

        assert resp['success'] is True
        assert resp['status'] == 200
        assert resp['message'] == 'Profile successful'
        assert resp['data']['name'] == default_user['data']['name']
        assert resp['data']['email'] == default_user['data']['email']

    def test_empty_auth_token(self):
        resp = self.get_user_profile('profile', '')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'No authentication token specified in x-auth-token header'

    def test_invalid_auth_token(self):
        resp = self.get_user_profile('profile', 'invalidToken')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'Access token is not valid or has expired, you will need to login'
