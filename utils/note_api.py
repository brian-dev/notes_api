from notes_api.utils.data_utils import fetch_endpoints


class NoteApi:
    endpoints = fetch_endpoints()

    def create_note(self, endpoint, title, desc, category, token, base_api):
        api_endpoint = self.endpoints[endpoint]
        payload = {
            'title': title,
            'description': desc,
            'category': category
        }

        resp = base_api.post_req_with_auth(api_endpoint, payload, token)
        return resp.json()

    def get_all_notes(self, endpoint, token, base_api):
        api_endpoint = self.endpoints[endpoint]

        resp = base_api.get_req_with_auth(api_endpoint, token)
        return resp.json()

    def get_note_by_id(self, endpoint, note_id, token, base_api):
        api_endpoint = self.endpoints[endpoint]
        note_endpoint = f"{api_endpoint}/{note_id}"

        resp = base_api.get_req_with_auth(note_endpoint, token)
        return resp.json()

    def del_note(self, endpoint, note_id, token, base_api):
        api_endpoint = self.endpoints[endpoint]
        note_endpoint = f"{api_endpoint}/{note_id}"

        resp = base_api.del_req(note_endpoint, token)
        return resp.json()
