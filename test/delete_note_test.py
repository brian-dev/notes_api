import random

from utils.api_utils import create_note, del_note, get_note_by_id
from utils.data_utils import generate_string_data


class TestDeleteNote:
    title = f"{generate_string_data(random.randrange(4, 15))}"
    desc = f"{generate_string_data(random.randrange(6, 15))}"

    def test_delete_note_resp(self, default_user, strings):
        new_note = create_note(strings['notes'], self.title, self.desc, 'Home',default_user['data']['token'])
        note_id = new_note['data']['id']

        note_to_delete = del_note(strings['notes'], note_id, default_user['data']['token'])

        assert note_to_delete['success'] is True
        assert note_to_delete['status'] == 200
        assert note_to_delete['message'] == 'Note successfully deleted'

    def test_delete_note_exists(self, default_user, strings):
        new_note = create_note(strings['notes'], self.title, self.desc, 'Home', default_user['data']['token'])
        note_id = new_note['data']['id']

        del_note(strings['notes'], note_id, default_user['data']['token'])
        deleted_note = get_note_by_id(strings['notes'], note_id, default_user['data']['token'])

        assert deleted_note['success'] is False
        assert deleted_note['status'] == 404
        assert deleted_note['message'] == 'No note was found with the provided ID, Maybe it was deleted'

    def test_delete_empty_token(self, default_user, strings):
        new_note = create_note(strings['notes'], self.title, self.desc, 'Home', default_user['data']['token'])
        note_id = new_note['data']['id']

        resp = del_note(strings['notes'], note_id, '')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'No authentication token specified in x-auth-token header'

    def test_delete_invalid_token(self, default_user, strings):
        new_note = create_note(strings['notes'], self.title, self.desc, 'Home', default_user['data']['token'])
        note_id = new_note['data']['id']

        resp = del_note(strings['notes'], note_id, 'invalidToken')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'Access token is not valid or has expired, you will need to login'



