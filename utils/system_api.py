from notes_api.utils.data_utils import fetch_endpoints


class SystemApi:
    endpoints = fetch_endpoints()

    def sys_check(self, endpoint, base_api):
        api_endpoint = self.endpoints[endpoint]
        resp = base_api.get_req(api_endpoint)
        return resp.json()
