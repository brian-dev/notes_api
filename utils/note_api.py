from utils.base_api import BaseApi


class NoteApi(BaseApi):
    def create_note(self, endpoint, title, desc, category, token):
        payload = {
            'title': title,
            'description': desc,
            'category': category
        }

        resp = self.post_req_with_auth(endpoint, payload, token)
        return resp.json()

    def get_all_notes(self, endpoint, token):
        resp = self.get_req(endpoint, token)
        return resp.json()

    def get_note_by_id(self, endpoint, note_id, token):
        note_endpoint = f"{endpoint}/{note_id}"
        resp = self.get_req(note_endpoint, token)
        return resp.json()

    def del_note(self, endpoint, note_id, token):
        note_endpoint = f"{endpoint}/{note_id}"
        resp = self.del_req(note_endpoint, token)
        return resp.json()