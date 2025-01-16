import requests
import json
import os

try:
    URLCREATEUSERclear = "http://127.0.0.1:9000/clear"
    URLDOCCREATEclear = "http://127.0.0.1:9001/clear"
    URLDOCSEARCHclear = "http://127.0.0.1:9002/clear"
    URLLOGclear = "http://127.0.0.1:9003/clear"
    r_clear = requests.get(url=URLLOGclear)
    r_clear = requests.get(url=URLCREATEUSERclear)
    r_clear = requests.get(url=URLDOCSEARCHclear)
    r_clear = requests.get(url=URLDOCCREATEclear)

    URLCREATEUSER = "http://127.0.0.1:9000/create_user"
    URLLOGIN = "http://127.0.0.1:9000/login"
    URLDOCCREATE = "http://127.0.0.1:9001/create_document"
    URLDOCEDIT = "http://127.0.0.1:9001/edit_document"
    URLDOCSEARCH = "http://127.0.0.1:9002/search"
    URLLOG = "http://127.0.0.1:9003/view_log"

    PARAMS = {'first_name': 'james', 'last_name': 'mariani', 'username': 'james', 'email_address': 'j@a.com',
              'password': 'Examplepassword1', 'group': 'instructors', 'salt': 'FE8x1gO+7z0B'}
    r = requests.post(url=URLCREATEUSER, data=PARAMS)
    data = r.json()

    PARAMS = {'first_name': 'abigail', 'last_name': 'murray', 'username': 'abigail', 'email_address': 'a@a.com',
              'password': 'Examplepassword1', 'group': 'instructors', 'salt': 'FE8x1gO+7z0B'}
    r = requests.post(url=URLCREATEUSER, data=PARAMS)
    data = r.json()

    CREATEDOCPARAMS = {'filename': 'a.txt', 'body': 'I will test project 3 better than I tested project 2',
                       'groups': json.dumps({'group1': 'instructors', 'group2': 'student', 'group3': 'smartfella'})}
    r_create = requests.post(url=URLDOCCREATE, data=CREATEDOCPARAMS, headers={
        'Authorization': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJqYW1lcyJ9.d5425b8034f430475313408dc6494622c8f1a373a16275c46d44f47d8d35fd52'})
    create_data = r_create.json()

    CREATEDOCPARAMS = {'filename': 'a.txt', 'body': 'I will test project 3 better than I tested project 2',
                       'groups': json.dumps({'group1': 'instructors', 'group2': 'student', 'group3': 'smartfella'})}
    r_create = requests.post(url=URLDOCCREATE, data=CREATEDOCPARAMS, headers={
        'Authorization': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJqYW1lcyJ9.d5425b8034f430475313408dc6494622c8f1a373a16275c46d44f47d8d35fd52'})
    create_data = r_create.json()

    EDITDOCPARAMS = {'filename': 'a.txt', 'body': '\nI promise I promise I promise to test better'}
    r_edit = requests.post(url=URLDOCEDIT, data=EDITDOCPARAMS, headers={
        'Authorization': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJhYmlnYWlsIn0=.9f8f49704d3cc7e898730f0ee2a0d92813b4b196ba5b9c16219139ceb4d2aab7'})
    edit_data = r_edit.json()

    SEARCHDOCPARAMS = {'filename': 'a.txt'}
    r_search = requests.get(url=URLDOCSEARCH, params=SEARCHDOCPARAMS, headers={
        'Authorization': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJqYW1lcyJ9.d5425b8034f430475313408dc6494622c8f1a373a16275c46d44f47d8d35fd52'})
    search_data = r_search.json()
    print(search_data)
except:
	print('Test Failed')