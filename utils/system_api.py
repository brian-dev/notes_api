from utils.base_api import BaseApi
from utils.data_utils import fetch_endpoints


class SystemApi(BaseApi):
    endpoints = fetch_endpoints()

    def sys_check(self, endpoint):
        api_endpoint = self.endpoints[endpoint]
        resp = self.get_req(api_endpoint)
        return resp.json()