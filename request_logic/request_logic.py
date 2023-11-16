import requests

from constants.constants import LOGIN, PASS


def send_request_get(user_id):
    response = requests.get('http://localhost:8080/oslic',
                            params={'id': user_id},
                            auth=(LOGIN, PASS)).json()
    return response


def send_request_post(user_data):
    response = requests.post('http://localhost:8080/oslic',
                             json=user_data,
                             auth=(LOGIN, PASS))
    return response


def send_request_delete(user_id):
    response = requests.delete('http://localhost:8080/oslic',
                               json={'id': user_id},
                               auth=(LOGIN, PASS))
    return response
