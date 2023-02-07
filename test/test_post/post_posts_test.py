import random
import requests
from utils.data_utils import generate_string_data, generate_timestamp
from utils.schema_utils import get_schema
from jsonschema import validate


class TestPostPosts:
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    user_id = random.randrange(1, 10)
    rand_string_length = random.randrange(8, 50)
    title = f"{generate_string_data(rand_string_length)} {generate_timestamp()}"
    body = f"{generate_string_data(rand_string_length)} {generate_timestamp()}"
    json = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    resp = requests.post(url=posts_url, json=json)

    def test_post_posts_resp_code(self):
        assert self.resp.status_code == 201

    def test_post_resp_data(self):
        resp = self.resp.json()
        assert resp['title'] == self.title
        assert resp['body'] == self.body
        assert resp['userId'] == self.user_id

    def test_validate_posts_resp_schema(self):
        schema = get_schema('posts')
        validate(instance=self.resp.json(), schema=schema)
