import random
import allure

from python_api.conftest import base_api
from python_api.utils.data_utils import generate_string_data
from python_api.utils.note_api import NoteApi


class TestDeleteNote(NoteApi):
    title = f"{generate_string_data(random.randrange(4, 15))}"
    desc = f"{generate_string_data(random.randrange(6, 15))}"

    @allure.feature('delete_note')
    def test_delete_note_resp(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Home', default_user[
            'data']['token'], base_api=base_api)
        note_id = new_note['data']['id']

        note_to_delete = self.del_note('notes', note_id, default_user['data']['token'], base_api=base_api)

        assert note_to_delete['success'] is True
        assert note_to_delete['status'] == 200
        assert note_to_delete['message'] == 'Note successfully deleted'

    @allure.feature('delete_note')
    def test_delete_note_exists(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Home', default_user['data']['token'],
                                    base_api=base_api)
        note_id = new_note['data']['id']

        self.del_note('notes', note_id, default_user['data']['token'], base_api=base_api)
        deleted_note = self.get_note_by_id(self.endpoints['notes'], note_id, default_user['data']['token'],
                                           base_api=base_api)

        assert deleted_note['success'] is False
        assert deleted_note['status'] == 404
        assert deleted_note['message'] == 'No note was found with the provided ID, Maybe it was deleted'

    @allure.feature('delete_note')
    def test_delete_empty_token(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Home', default_user['data']['token'],
                                    base_api=base_api)
        note_id = new_note['data']['id']

        resp = self.del_note('notes', note_id, '', base_api=base_api)

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'No authentication token specified in x-auth-token header'

    @allure.feature('delete_note')
    def test_delete_invalid_token(self, default_user):
        new_note = self.create_note('notes', self.title, self.desc, 'Home', default_user['data']['token'],
                                    base_api=base_api)
        note_id = new_note['data']['id']

        resp = self.del_note('notes', note_id, 'invalidToken', base_api=base_api)

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'Access token is not valid or has expired, you will need to login'
