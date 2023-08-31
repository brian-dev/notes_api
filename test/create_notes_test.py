import random

from utils.api_utils import create_note
from utils.data_utils import generate_string_data


class TestCreateNotes:
    title = f"{generate_string_data(random.randrange(4, 15))}"
    desc = f"{generate_string_data(random.randrange(6, 15))}"

    def test_create_new_note(self, login):
        token = login['data']['token']
        cat_vals = ['Home', 'Work', 'Personal']

        for cat in cat_vals:
            resp = create_note(self.title, self.desc, cat, token)
            json_vals = resp.json()

            assert json_vals['success'] is True
            assert json_vals['status'] == 200
            assert json_vals['message'] == 'Note successfully created'
            assert json_vals['data']['title'] == self.title
            assert json_vals['data']['description'] == self.desc
            assert json_vals['data']['category'] == cat
            assert json_vals['data']['completed'] is False

    def test_create_note_invalid_title(self, login):
        token = login['data']['token']
        title_vals = ['', 'abc', generate_string_data(random.randrange(101, 105))]

        for title in title_vals:
            resp = create_note(title, self.desc, 'Home', token)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == 'Title must be between 4 and 100 characters'

    def test_create_note_invalid_desc(self, login):
        token = login['data']['token']
        desc_vals = ['', 'abc', generate_string_data(random.randrange(1001, 1005))]

        for desc in desc_vals:
            resp = create_note(self.title, desc, 'Home', token)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == 'Description must be between 4 and 1000 characters'

    def test_create_note_invalid_category(self, login):
        token = login['data']['token']
        cat_vals = ['', 'abc']

        for cat in cat_vals:
            resp = create_note(self.title, self.desc, cat, token)
            json_vals = resp.json()

            assert json_vals['success'] is False
            assert json_vals['status'] == 400
            assert json_vals['message'] == 'Category must be one of the categories: Home, Work, Personal'

    def test_create_note_empty_token(self, login):
        resp = create_note(self.title, self.desc, 'Home', '')
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == 'No authentication token specified in x-auth-token header'

    def test_create_note_invalid_token(self, login):
        resp = create_note(self.title, self.desc, 'Home', 'invalidToken')
        json_vals = resp.json()

        assert json_vals['success'] is False
        assert json_vals['status'] == 401
        assert json_vals['message'] == 'Access token is not valid or has expired, you will need to login'
