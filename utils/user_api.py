from utils.base_api import BaseApi


class UserApi(BaseApi):
    def register_new_user(self, payload):
        endpoint = 'users/register'

        resp = self.post_req(endpoint, payload)
        if resp.status_code != 201:
            raise Exception(f"Request failed. {resp.json()}")
        return resp.json()

    def login_user(self, user_creds):
        endpoint = 'users/login'

        resp = self.post_req(endpoint, user_creds)
        if resp.status_code != 200:
            raise Exception(f"Request failed. {resp.json()}")
        return resp.json()

    def delete_user(self, token):
        endpoint = 'users/delete-account'

        resp = self.del_req(endpoint, token)
        if resp.status_code != 200:
            raise Exception(f"Request failed. {resp.json()}")
        return resp.json()