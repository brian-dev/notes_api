from notes_api.utils.data_utils import fetch_endpoints


class UserApi:
    endpoints = fetch_endpoints()

    def register_new_user(self, endpoint, payload, base_api):
        resp = base_api.post_req(self.endpoints[endpoint], payload)
        return resp.json()

    def login_user(self, endpoint, user_creds, base_api):
        api_endpoint = self.endpoints[endpoint]

        resp = base_api.post_req(api_endpoint, user_creds)
        return resp.json()

    def delete_user(self, endpoint, token, base_api):
        resp = base_api.del_req(self.endpoints[endpoint], token)
        if resp.status_code != 200:
            raise Exception(f"Request failed. {resp.json()}")
        return resp.json()

    def get_user_profile(self, endpoint, token, base_api):
        resp = base_api.get_req_with_auth(self.endpoints[endpoint], token)
        return resp.json()

    def update_user_profile(self, endpoint, payload, token, base_api):
        resp = base_api.patch_req_with_auth(self.endpoints[endpoint], payload, token)
        return resp.json()
