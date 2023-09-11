import random

import allure

from utils.note_api import NoteApi
from utils.data_utils import generate_string_data


class TestCreateNotes(NoteApi):
    title = f"{generate_string_data(random.randrange(4, 15))}"
    desc = f"{generate_string_data(random.randrange(6, 15))}"

    @allure.feature('create_note')
    def test_create_new_note(self, default_user):
        cat_vals = ['Home', 'Work', 'Personal']

        for cat in cat_vals:
            resp = self.create_note('notes', self.title, self.desc, cat, default_user[
                'data']['token'])

            assert resp['success'] is True
            assert resp['status'] == 200
            assert resp['message'] == 'Note successfully created'
            assert resp['data']['title'] == self.title
            assert resp['data']['description'] == self.desc
            assert resp['data']['category'] == cat
            assert resp['data']['completed'] is False

    @allure.feature('create_note')
    def test_create_note_invalid_title(self, default_user):
        title_vals = ['', 'abc', generate_string_data(random.randrange(101, 105))]

        for title in title_vals:
            resp = self.create_note('notes', title, self.desc, 'Home', default_user['data'][
                'token'])

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == 'Title must be between 4 and 100 characters'

    @allure.feature('create_note')
    def test_create_note_invalid_desc(self, default_user):
        desc_vals = ['', 'abc', generate_string_data(random.randrange(1001, 1005))]

        for desc in desc_vals:
            resp = self.create_note('notes', self.title, desc, 'Home', default_user['data'][
                'token'])

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == 'Description must be between 4 and 1000 characters'

    @allure.feature('create_note')
    def test_create_note_invalid_category(self, default_user):
        cat_vals = ['', 'abc']

        for cat in cat_vals:
            resp = self.create_note('notes', self.title, self.desc, cat, default_user['data'][
                'token'])

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == 'Category must be one of the categories: Home, Work, Personal'

    @allure.feature('create_note')
    def test_create_note_empty_token(self):
        resp = self.create_note('notes', self.title, self.desc, 'Home', '')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'No authentication token specified in x-auth-token header'

    @allure.feature('create_note')
    def test_create_note_invalid_token(self):
        resp = self.create_note('notes', self.title, self.desc, 'Home', 'invalidToken')

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == 'Access token is not valid or has expired, you will need to login'
