import random
import requests
from jsonschema import validate
from utils.schema_utils import get_schema


class TestGetPhotos:
    photos_url = 'https://jsonplaceholder.typicode.com/photos'
    resp = requests.get(photos_url)

    def test_get_photos_resp_code(self):
        assert self.resp.status_code == 200

    def test_get_photos_all_items_returned(self):
        photo_ids = []
        for item in self.resp.json():
            photo_ids.append(item["id"])
        assert len(photo_ids) == 5000

    def test_validate_get_photos_schema(self):
        photo_id = random.randrange(1, 5000)
        resp = requests.get(f'{self.photos_url}/{photo_id}').json()
        schema = get_schema('photos')
        validate(instance=resp, schema=schema)
