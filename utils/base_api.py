import os
import requests

from dotenv import load_dotenv


def auth_headers(token):
    return {'x-auth-token': token}


class BaseApi:
    load_dotenv()
    base_url = os.getenv('BASE_URL')

    def post_req(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, payload)

    def post_req_with_auth(self, endpoint, payload, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, payload, headers=auth_headers(token))

    def del_req(self, endpoint, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.delete(url, headers=auth_headers(token))

    def get_req(self, endpoint, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, headers=auth_headers(token))

    def patch_req_with_auth(self, endpoint, payload, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.patch(url, payload, headers=auth_headers(token))
