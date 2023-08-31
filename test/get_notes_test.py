from utils.api_utils import get_note


class TestGetNotes:

    def test_get_all_user_notes(self, login):
        token = login['data']['token']
        notes = get_note('notes', token)

        json_vals = notes.json()

        assert json_vals['success'] is True
        assert json_vals['status'] == 200
        assert json_vals['message'] == 'Notes successfully retrieved'

