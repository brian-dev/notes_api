import os
import requests
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('BASE_URL')


def auth_headers(token):
    return {'x-auth-token': token}


def post_req(endpoint, payload):
    url = f"{base_url}/{endpoint}"
    return requests.post(url, payload)


def post_req_with_auth(endpoint, payload, token):
    url = f"{base_url}/{endpoint}"
    return requests.post(url, payload, headers=auth_headers(token))


def del_req(endpoint, token):
    url = f"{base_url}/{endpoint}"
    return requests.delete(url, headers=auth_headers(token))


def get_req(endpoint, token):
    url = f"{base_url}/{endpoint}"
    return requests.get(url, headers=auth_headers(token))


def register_new_user(payload):
    endpoint = 'users/register'

    resp = post_req(endpoint, payload)
    if resp.status_code != 201:
        raise Exception(f"Request failed. {resp.json()}")
    return resp.json()


def login_user(user_creds):
    endpoint = 'users/login'

    resp = post_req(endpoint, user_creds)
    if resp.status_code != 200:
        raise Exception(f"Request failed. {resp.json()}")
    return resp.json()


def delete_user(token):
    endpoint = 'users/delete-account'

    resp = del_req(endpoint, token)
    if resp.status_code != 200:
        raise Exception(f"Request failed. {resp.json()}")
    return resp.json()


def create_note(endpoint, title, desc, category, token):
    payload = {
        'title': title,
        'description': desc,
        'category': category
    }

    resp = post_req_with_auth(endpoint, payload, token)
    return resp.json()


def get_all_notes(endpoint, token):
    resp = get_req(endpoint, token)
    return resp.json()


def get_note_by_id(endpoint, note_id, token):
    note_endpoint = f"{endpoint}/{note_id}"
    resp = get_req(note_endpoint, token)
    return resp.json()


def del_note(endpoint, note_id, token):
    note_endpoint = f"{endpoint}/{note_id}"
    resp = del_req(note_endpoint, token)
    return resp.json()
