import requests

USER_PORT = "5000"
MANAGER_PORT = "5000"
SEARCH_PORT = "5000"
LOG_PORT = "5000"
MANAGER_MICRO = f"http://docs-micro:{MANAGER_PORT}"
SEARCH_MICRO = f"http://search-micro:{SEARCH_PORT}"
USER_MICRO = f"http://user-micro:{USER_PORT}"
LOG_MICRO = f"http://logs-micro:{LOG_PORT}"

def get_doc_groups(filename):
    r = requests.get(MANAGER_MICRO+'/doc_groups', params={'filename': filename})
    groups = r.json()["doc_groups"]
    return groups


def user_group_in_doc_groups(filename, user_group) -> bool:
    for doc_group in get_doc_groups(filename):
        if user_group == doc_group:
            return True
    return False


def log_event(event, user, filename=None):
    MICRO2URL = "http://localhost:5003/create_log"
    CREATEDOCPARAMS = {'event': event, 'username': user}

    if filename:
        CREATEDOCPARAMS['filename'] = filename

    requests.post(url=LOG_MICRO+'/create_log', data=CREATEDOCPARAMS)