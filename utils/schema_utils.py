import json


def get_schema(schema_type):
    # This function loads the given schema available
    with open(f'./schema/{schema_type}_schema.json', 'r') as file:
        schema = json.load(file)
    return schema
