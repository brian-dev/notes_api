from utils.api_utils import get_all_notes


class TestGetNotes:

    def test_get_all_user_notes(self, default_user, strings):
        notes = get_all_notes(strings['notes'], default_user['data']['token'])

        assert notes['success'] is True
        assert notes['status'] == 200
        assert notes['message'] == 'Notes successfully retrieved'

