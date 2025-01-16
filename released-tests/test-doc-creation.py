import requests
import json
import os

try:

    URLDOCCREATE = "http://127.0.0.1:9001/create_document"
    URLDOCCLEAR = "http://127.0.0.1:9001/clear"
    r_clear = requests.get(url=URLDOCCLEAR)

    CREATEDOCPARAMS = {'filename': 'b.txt', 'body': 'I will test project 3 better than I tested project 2',
                       'groups': json.dumps({'group1': 'instructors', 'group2': 'student', 'group3': 'smartfella'})}
    r_create = requests.post(url=URLDOCCREATE, data=CREATEDOCPARAMS, headers={
        'Authorization': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJqYW1lcyJ9.d5425b8034f430475313408dc6494622c8f1a373a16275c46d44f47d8d35fd52'})
    create_data = r_create.json()

    CREATEDOCPARAMS = {'filename': 'b.txt', 'body': 'I will test project 3 better than I tested project 2, rioaierngioarnhogiaernorgnairgniorngornaoirgn ',
                       'groups': json.dumps({'group1': 'instructors', 'group2': 'student', 'group3': 'smartfella'})}
    r_create = requests.post(url=URLDOCCREATE, data=CREATEDOCPARAMS, headers={
        'Authorization': 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJqYW1lcyJ9.d5425b8034f430475313408dc6494622c8f1a373a16275c46d44f47d8d35fd52'})
    create_data = r_create.json()
    print(create_data)
except:
	print('Test Failed')