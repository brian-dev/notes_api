from utils.base_api import BaseApi
from utils.data_utils import fetch_endpoints


class NoteApi(BaseApi):
    endpoints = fetch_endpoints()

    def create_note(self, endpoint, title, desc, category, token):
        api_endpoint = self.endpoints[endpoint]
        payload = {
            'title': title,
            'description': desc,
            'category': category
        }

        resp = self.post_req_with_auth(api_endpoint, payload, token)
        return resp.json()

    def get_all_notes(self, endpoint, token):
        api_endpoint = self.endpoints[endpoint]

        resp = self.get_req_with_auth(api_endpoint, token)
        return resp.json()

    def get_note_by_id(self, endpoint, note_id, token):
        api_endpoint = self.endpoints[endpoint]
        note_endpoint = f"{api_endpoint}/{note_id}"

        resp = self.get_req_with_auth(note_endpoint, token)
        return resp.json()

    def del_note(self, endpoint, note_id, token):
        api_endpoint = self.endpoints[endpoint]
        note_endpoint = f"{api_endpoint}/{note_id}"

        resp = self.del_req(note_endpoint, token)
        return resp.json()
