import sqlite3
import os
import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=(['GET']))
def index():

	return json.dumps({'1': 'test', '2': 'test2'})

@app.route('/test_micro', methods=(['GET']))
def test_micro():

	return json.dumps({"response": "This is a message from Microservice 2"})

