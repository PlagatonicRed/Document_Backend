import requests

USER_PORT = "5000"
MANAGER_PORT = "5000"
SEARCH_PORT = "5000"
LOG_PORT = "5000"
MANAGER_MICRO = f"http://docs-micro:{MANAGER_PORT}"
SEARCH_MICRO = f"http://search-micro:{SEARCH_PORT}"
USER_MICRO = f"http://user-micro:{USER_PORT}"
LOG_MICRO = f"http://logs-micro:{LOG_PORT}"

def get_doc_auth(filename, username):
    r = requests.get(USER_MICRO+'/doc_auth', params={'username': username, 'filename': filename})
    doc_auth = r.json()["doc_auth"]
    return doc_auth