from flask import Blueprint, request, jsonify
from utils.auth import validate_jwt
from utils.database import get_db
from utils.doc_creation import handle_doc_creation
from utils.doc_editing import append_text_file, update_doc_db
from utils.doc_info import get_doc_hash, get_doc_owner, get_doc_groups,get_doc_path
from utils.micro_info import get_user_group, get_doc_auth, log_event
import base64

doc_bp = Blueprint('doc', __name__)


@doc_bp.route('/create_document', methods=['POST'])
def create_doc():
    db = get_db()
    try:
        filename = request.form.get('filename')
        body = request.form.get('body')
        groups = request.form.get('groups')

        jwt = validate_jwt(request.headers.get('Authorization'))
        if jwt is None:
            return jsonify({'status': 2})

        username = jwt.get("username")

        handle_doc_creation(username, filename, body, groups)
        db.commit()
        print("Doc created successfully")
        log_event('document_creation', username, filename)
        return jsonify({"status": 1})

    except Exception as e:
        db.rollback()
        print(f"Document creation database insertion failed {e}")

    finally:
        db.close()


@doc_bp.route('/edit_document', methods=['POST'])
def edit_doc():
    db = get_db()
    try:
        filename = request.form.get('filename')
        body = request.form.get('body')

        jwt = validate_jwt(request.headers.get('Authorization'))
        if jwt is None:
            return jsonify({'status': 2})

        username = jwt.get("username")

        if not get_doc_auth(filename, username):
            print("authorization failed")
            return jsonify({'status': 3})

        print("authorization successful")
        append_text_file(filename, body)
        print("Doc edited successfully")
        update_doc_db(filename)

        log_event('document_edit', username, filename)

        return jsonify({"status": 1})

    except Exception as e:
        db.rollback()
        print(f"Document editing failed {e}")

    finally:
        db.close()


@doc_bp.route('/doc_hash', methods=(['GET']))
def doc_hash():
    file_path = get_doc_path(request.args.get('filename'))
    return jsonify({"doc_hash": get_doc_hash(file_path)})


@doc_bp.route('/doc_owner', methods=(['GET']))
def doc_owner():
    owner = get_doc_owner(request.args.get('filename'))
    return jsonify({"doc_owner": owner})


@doc_bp.route('/doc_groups', methods=(['GET']))
def doc_groups():
    groups = get_doc_groups(request.args.get('filename'))
    return jsonify({"doc_groups": groups})
