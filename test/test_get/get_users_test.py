import random
import requests
from jsonschema import validate
from utils.schema_utils import get_schema


class TestGetUsers:
    users_url = 'https://jsonplaceholder.typicode.com/users'
    resp = requests.get(users_url)

    def test_get_users_resp_code(self):
        assert self.resp.status_code == 200

    def test_get_users_all_items_returned(self):
        user_ids = []
        for item in self.resp.json():
            user_ids.append(item["id"])
        assert len(user_ids) == 10

    def test_validate_get_users_schema(self):
        user_id = random.randrange(1, 10)
        resp = requests.get(f'{self.users_url}/{user_id}').json()
        schema = get_schema('users')
        validate(instance=resp, schema=schema)
