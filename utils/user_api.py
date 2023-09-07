from utils.base_api import BaseApi
from utils.data_utils import fetch_endpoints


class UserApi(BaseApi):
    endpoints = fetch_endpoints()

    def register_new_user(self, endpoint, payload):
        resp = self.post_req(self.endpoints[endpoint], payload)
        return resp.json()

    def login_user(self, endpoint, user_creds):
        api_endpoint = self.endpoints[endpoint]

        resp = self.post_req(api_endpoint, user_creds)
        return resp.json()

    def delete_user(self, endpoint, token):
        resp = self.del_req(self.endpoints[endpoint], token)
        if resp.status_code != 200:
            raise Exception(f"Request failed. {resp.json()}")
        return resp.json()

    def get_user_profile(self, endpoint, token):
        resp = self.get_req_with_auth(self.endpoints[endpoint], token)
        return resp.json()

    def update_user_profile(self, endpoint, payload, token):
        resp = self.patch_req_with_auth(self.endpoints[endpoint], payload, token)
        return resp.json()
