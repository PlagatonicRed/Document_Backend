from flask import Blueprint, request, jsonify
from utils.database import get_db
from utils.auth import hash_sha256, decode_jwt
from utils.micro_info import log_event
from utils.validation import password_validation2, username_taken, email_taken
from utils.user import get_user_group
user_bp = Blueprint('user', __name__)


@user_bp.route('/create_user', methods=['POST'])
def create_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    email_address = request.form.get('email_address')
    password = request.form.get('password')
    salt = request.form.get('salt')
    user_group = request.form.get('group')

    db = get_db()
    cursor = db.cursor()
    try:
        if username_taken(username):
            print("Username taken")
            return jsonify({"status": 2, "pass_hash": "NULL"})

        if email_taken(email_address):
            print("Email taken")
            return jsonify({"status": 3, "pass_hash": "NULL"})

        if not password_validation2(username, password, salt, first_name, last_name):
            print("Invalid password")
            return jsonify({"status": 4, "pass_hash": "NULL"})

        hashed_password = hash_sha256(password + salt)

        query = """
        INSERT INTO users (first_name, last_name, username, email_address, password, salt, user_group) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (first_name, last_name, username, email_address, hashed_password, salt, user_group))
        db.commit()

        log_event('user_creation', username)

        return jsonify({"status": 1, "pass_hash": hashed_password})

    except Exception as e:
        print(f"User creation failed: {e}")

    finally:

        db.close()


@user_bp.route('/user_group', methods=(['GET']))
def user_groups():
    user_group = get_user_group(request.args.get('username'))
    return jsonify({"user_group": user_group})
