from utils.base_api import BaseApi


class SystemApi(BaseApi):
    def sys_check(self, endpoint):
        resp = self.get_req(endpoint)
        return resp.json()