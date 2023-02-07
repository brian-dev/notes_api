import random
import requests
from jsonschema import validate
from utils.schema_utils import get_schema


class TestGetAlbums:
    albums_url = 'https://jsonplaceholder.typicode.com/albums'
    resp = requests.get(albums_url)

    def test_get_albums_resp_code(self):
        assert self.resp.status_code == 200

    def test_get_albums_all_items_returned(self):
        album_ids = []
        for item in self.resp.json():
            album_ids.append(item["id"])
        assert len(album_ids) == 100

    def test_validate_get_albums_schema(self):
        album_id = random.randrange(1, 100)
        resp = requests.get(f'{self.albums_url}/{album_id}').json()
        schema = get_schema('albums')
        validate(instance=resp, schema=schema)
