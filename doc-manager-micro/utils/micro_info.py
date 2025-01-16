import requests

USER_PORT = "5000"
MANAGER_PORT = "5000"
SEARCH_PORT = "5000"
LOG_PORT = "5000"
MANAGER_MICRO = f"http://docs-micro:{MANAGER_PORT}"
SEARCH_MICRO = f"http://search-micro:{SEARCH_PORT}"
USER_MICRO = f"http://user-micro:{USER_PORT}"
LOG_MICRO = f"http://logs-micro:{LOG_PORT}"
def get_user_group(username):
    r = requests.get(USER_MICRO+'/user_group', params={'username': username})
    user_group = r.json()["user_group"]
    return user_group


def get_doc_auth(filename, username):
    r = requests.get(USER_MICRO+'/doc_auth', params={'username': username, 'filename': filename})
    doc_auth = r.json()["doc_auth"]
    return doc_auth


def log_event(event, user, filename=None):
    CREATEDOCPARAMS = {'event': event, 'username': user}

    if filename:
        CREATEDOCPARAMS['filename'] = filename

    requests.post(url=LOG_MICRO+'/create_log', data=CREATEDOCPARAMS)

