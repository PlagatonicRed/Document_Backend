import requests
from flask import Blueprint, request, jsonify

from utils.auth import validate_jwt
from utils.database import get_db
from utils.logging import log_event, get_formatted_logs, get_doc_logs, get_user_logs, get_doc_last_mod, \
    get_doc_total_mod
from utils.micro_info import get_doc_auth

logging_bp = Blueprint('logs', __name__)


@logging_bp.route('/view_log', methods=['GET'])
def view_log():
    db = get_db()
    try:
        data = {}
        filename = request.args.get('filename')
        username = request.args.get('username')

        jwt = validate_jwt(request.headers.get('Authorization'))
        if jwt is None:
            return jsonify({'status': 2, 'data': 'NULL'})

        requestor = jwt.get("username")

        if username is None:
            if not get_doc_auth(filename, requestor):
                print("The user does not have authorization for this document")
                return jsonify({'status': 3, 'data': 'NULL'})
            data = get_formatted_logs(get_doc_logs(filename))
        else:
            if username != requestor:
                print("you cannot view other users logs")
                return jsonify({'status': 3, 'data': 'NULL'})
            data = get_formatted_logs(get_user_logs(username))

        print("\n\n")
        print(data)
        print("\n\n")
        return jsonify({'status': 1, 'data': data})

    except Exception as e:
        print(f"Log viewing failed: {e}")

    finally:
        db.close()


@logging_bp.route('/create_log', methods=['POST'])
def create_log():
    db = get_db()
    try:
        event = request.form.get('event')
        username = request.form.get('username')
        filename = request.form.get('filename')

        if filename is None:
            log_event(event, username)
        else:
            log_event(event, username, filename)
        return jsonify({'status': 1})
    except Exception as e:
        db.rollback()
        print(f"Log creation failed: {e}")

    finally:
        db.close()


@logging_bp.route('/doc_last_mod', methods=['GET'])
def doc_last_mod():
    filename = request.args.get('filename')
    return jsonify({"doc_last_mod": get_doc_last_mod(filename)})


@logging_bp.route('/doc_total_mod', methods=['GET'])
def doc_total_mod():
    filename = request.args.get('filename')
    return jsonify({"doc_total_mod": get_doc_total_mod(filename)})