import hashlib
import sys

import requests

USER_PORT = "5000"
MANAGER_PORT = "5000"
SEARCH_PORT = "5000"
LOG_PORT = "5000"
MANAGER_MICRO = f"http://docs-micro:{MANAGER_PORT}"
SEARCH_MICRO = f"http://search-micro:{SEARCH_PORT}"
USER_MICRO = f"http://user-micro:{USER_PORT}"
LOG_MICRO = f"http://logs-micro:{LOG_PORT}"


def get_doc_hash(filename):
    r = requests.get(MANAGER_MICRO+'/doc_hash', params={'filename': filename})
    path = r.json()["doc_hash"]
    return path


def get_doc_owner(filename):

    r = requests.get(MANAGER_MICRO+'/doc_owner', params={'filename': filename})
    owner = r.json()["doc_owner"]
    return owner


def get_doc_last_mod(filename):
    r = requests.get(LOG_MICRO+'/doc_last_mod', params={'filename': filename})
    last_mod = r.json()["doc_last_mod"]
    return last_mod


def get_doc_total_mod(filename):
    r = requests.get(LOG_MICRO+'/doc_total_mod', params={'filename': filename})
    total_mod = r.json()["doc_total_mod"]
    return total_mod






def get_doc_auth(filename, username):
    r = requests.get(USER_MICRO+'/doc_auth', params={'username': username, 'filename': filename})
    doc_auth = r.json()["doc_auth"]
    return doc_auth


def log_event(event, user, filename=None):
    CREATEDOCPARAMS = {'event': event, 'username': user}

    if filename:
        CREATEDOCPARAMS['filename'] = filename

    requests.post(url=LOG_MICRO+'/create_log', data=CREATEDOCPARAMS)