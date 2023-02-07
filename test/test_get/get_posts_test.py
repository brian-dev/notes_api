import random
import requests
from jsonschema import validate
from utils.schema_utils import get_schema


class TestGetPosts:
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    resp = requests.get(posts_url)

    def test_get_posts_resp_code(self):
        assert self.resp.status_code == 200

    def test_get_posts_all_items_returned(self):
        post_ids = []
        for item in self.resp.json():
            post_ids.append(item["id"])
        assert len(post_ids) == 100

    def test_validate_get_posts_schema(self):
        post_id = random.randrange(1, 100)
        resp = requests.get(f'{self.posts_url}/{post_id}').json()
        schema = get_schema('posts')
        validate(instance=resp, schema=schema)
