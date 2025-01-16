from flask import Blueprint, request, jsonify
from utils.auth import encode_jwt, hash_sha256
from utils.micro_info import user_group_in_doc_groups, log_event
from utils.database import get_db
from utils.user import get_user_data, get_user_group
import os

auth_bp = Blueprint('auth', __name__)

key_file = os.path.join(os.path.dirname(__file__), 'key.txt')

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({"status": 2, "jwt" : "NULL"})
    db = get_db()
    try:

        # Check the database for the user
        user = get_user_data(username)
    finally:
        db.commit()
        db.close()

    # If the user doesn't exist or the password doesn't match
    if user is None or user[5] != hash_sha256(password + user[6]):
        return jsonify({"status": 2, "jwt" : "NULL"})

    # Create JWT Payload
    payload = {
        "username": user[3]
    }


    with open(key_file, 'r') as file:
        secret_key = file.read().strip()

    # Generate JWT
    token = encode_jwt(payload, secret_key)

    # Return the token in the response
    log_event('login', username)

    return jsonify({"status": 1, "jwt": token})


@auth_bp.route('/doc_auth', methods=['GET'])
def doc_auth():
    username = request.args.get('username')
    filename = request.args.get('filename')
    return jsonify({"doc_auth": user_group_in_doc_groups(filename, get_user_group(username))})


