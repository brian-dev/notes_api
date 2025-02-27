import random
import allure

from notes_api.conftest import base_api
from notes_api.utils.data_utils import generate_string_data
from notes_api.utils.note_api import NoteApi


class TestGetNotes(NoteApi):
    title = f"{generate_string_data(random.randrange(4, 15))}"
    desc = f"{generate_string_data(random.randrange(6, 15))}"

    @allure.feature('get_note')
    def test_get_all_user_notes(self, default_user):
        notes = self.get_all_notes('notes', default_user['data']['token'], base_api=base_api)

        assert notes['success'] is True
        assert notes['status'] == 200
        assert notes['message'] == 'Notes successfully retrieved'

    @allure.feature('get_note')
    def test_get_all_user_notes_empty_token(self, default_user):
        notes = self.get_all_notes('notes', '', base_api=base_api)

        assert notes['success'] is False
        assert notes['status'] == 401
        assert notes['message'] == 'No authentication token specified in x-auth-token header'

    @allure.feature('get_note')
    def test_get_all_user_notes_invalid_token(self, default_user):
        notes = self.get_all_notes('notes', 'invalidToken', base_api=base_api)

        assert notes['success'] is False
        assert notes['status'] == 401
        assert notes['message'] == 'Access token is not valid or has expired, you will need to login'

    @allure.feature('get_note')
    def test_get_note_by_id(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Work', default_user['data']['token'],
                                    base_api=base_api)
        note_id = new_note['data']['id']

        resp = self.get_note_by_id('notes', note_id, default_user['data']['token'], base_api=base_api)

        assert resp['success'] is True
        assert resp['status'] == 200
        assert resp['message'] == 'Note successfully retrieved'
        assert resp['data']['title'] == self.title
        assert resp['data']['description'] == self.desc
        assert resp['data']['category'] == 'Work'
        assert resp['data']['completed'] is False

    @allure.feature('get_note')
    def get_note_by_id_empty_token(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Work', default_user['data']['token'],
                                    base_api=base_api)
        note_id = new_note['data']['id']

        resp = self.get_note_by_id('notes', note_id, '', base_api=base_api)

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'No authentication token specified in x-auth-token header'

    @allure.feature('get_note')
    def get_note_by_id_invalid_token(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Work', default_user['data']['token'],
                                    base_api=base_api)
        note_id = new_note['data']['id']

        resp = self.get_note_by_id('notes', note_id, 'invalidToken', base_api=base_api)

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'Access token is not valid or has expired, you will need to login'
