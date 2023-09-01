import random

from utils.data_utils import generate_string_data
from utils.note_api import NoteApi


class TestGetNotes(NoteApi):
    title = f"{generate_string_data(random.randrange(4, 15))}"
    desc = f"{generate_string_data(random.randrange(6, 15))}"

    def test_get_all_user_notes(self, default_user):
        notes = self.get_all_notes('notes', default_user['data']['token'])

        assert notes['success'] is True
        assert notes['status'] == 200
        assert notes['message'] == 'Notes successfully retrieved'

    def test_get_all_user_notes_empty_token(self, default_user):
        notes = self.get_all_notes('notes', '')

        assert notes['success'] is False
        assert notes['status'] == 401
        assert notes['message'] == 'No authentication token specified in x-auth-token header'

    def test_get_all_user_notes_invalid_token(self, default_user):
        notes = self.get_all_notes('notes', 'invalidToken')

        assert notes['success'] is False
        assert notes['status'] == 401
        assert notes['message'] == 'Access token is not valid or has expired, you will need to login'

    def test_get_note_by_id(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Work', default_user['data']['token'])
        note_id = new_note['data']['id']

        resp = self.get_note_by_id('notes', note_id, default_user['data']['token'])

        assert resp['success'] is True
        assert resp['status'] == 200
        assert resp['message'] == 'Note successfully retrieved'
        assert resp['data']['title'] == self.title
        assert resp['data']['description'] == self.desc
        assert resp['data']['category'] == 'Work'
        assert resp['data']['completed'] is False

    def get_note_by_id_empty_token(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Work', default_user['data']['token'])
        note_id = new_note['data']['id']

        resp = self.get_note_by_id('notes', note_id, '')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'No authentication token specified in x-auth-token header'

    def get_note_by_id_invalid_token(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Work', default_user['data']['token'])
        note_id = new_note['data']['id']

        resp = self.get_note_by_id('notes', note_id, 'invalidToken')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'Access token is not valid or has expired, you will need to login'
