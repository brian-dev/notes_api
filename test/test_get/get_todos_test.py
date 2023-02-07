import random
import requests
from jsonschema import validate
from utils.schema_utils import get_schema


class TestGetToDos:
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    resp = requests.get(todos_url)

    def test_get_todos_resp_code(self):
        assert self.resp.status_code == 200

    def test_get_todos_all_items_returned(self):
        todo_ids = []
        for item in self.resp.json():
            todo_ids.append(item["id"])
        assert len(todo_ids) == 200

    def test_validate_get_todos_schema(self):
        todo_id = random.randrange(1, 200)
        resp = requests.get(f'{self.todos_url}/{todo_id}').json()
        schema = get_schema('todos')
        validate(instance=resp, schema=schema)
