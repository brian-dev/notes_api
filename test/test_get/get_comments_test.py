import random
import requests
from jsonschema import validate
from utils.schema_utils import get_schema


class TestGetComments:
    comments_url = 'https://jsonplaceholder.typicode.com/comments'
    resp = requests.get(comments_url)

    def test_get_comments_resp_code(self):
        assert self.resp.status_code == 200

    def test_get_comments_all_items_returned(self):
        comment_ids = []
        for item in self.resp.json():
            comment_ids.append(item["id"])
        assert len(comment_ids) == 500

    def test_validate_get_comments_schema(self):
        comment_id = random.randrange(1, 500)
        resp = requests.get(f'{self.comments_url}/{comment_id}').json()
        schema = get_schema('comments')
        validate(instance=resp, schema=schema)
