import random
import requests

from utils.data_utils import generate_string_data


# def auth_headers(token):
#     return {'x-auth-token': token}
#
#
# class TestUpdateUserProfile:
#     profile_endpoint = 'users/profile'
#
#     def test_update_user_name(self, base_url, login):
#         url = f"{base_url}/{self.profile_endpoint}"
#         headers = auth_headers(login['data']['token'])
#         name = f"{generate_string_data(random.randrange(4, 15))}"
#
#         resp = requests.patch(url, json={'name': name}, headers=headers)
#         json_vals = resp.json()
#         assert json_vals['success'] is True
#         assert json_vals['status'] == 200
#         assert json_vals['message'] == 'Profile updated successful'
#         assert json_vals['data']['name'] == 'tester'
#         assert json_vals['data']['email'] == 'a@example.com'
#
#         requests.patch(url, json={'name': login['data']['name']}, headers=headers)
