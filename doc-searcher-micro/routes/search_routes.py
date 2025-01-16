import requests
from flask import Blueprint, request, jsonify

from utils.auth import validate_jwt
from utils.database import get_db
from utils.micro_info import get_doc_owner, get_doc_hash, get_doc_auth, log_event, get_doc_total_mod, get_doc_last_mod

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=(['GET']))
def search():
    db = get_db()
    try:


        jwt = validate_jwt(request.headers.get('Authorization'))
        if jwt is None:
            return jsonify({'status': 2, 'data': 'NULL'})

        username = jwt.get("username")
        filename = request.args.get('filename')

        if not get_doc_auth(filename, username):
            return jsonify({'status': 3, 'data': 'NULL'})

        print("DATA----------------------\n")
        print("filename: " + filename)
        owner = get_doc_owner(filename)
        print("owner: " + owner)
        last_mod = get_doc_last_mod(filename)
        print("last_mod: " + last_mod)
        total_mod = get_doc_total_mod(filename)
        print(total_mod)

        hash = get_doc_hash(filename)
        print(hash)

        data = {}
        data['filename'] = filename
        data['owner'] = owner
        data['last_mod'] = last_mod
        data['total_mod'] = total_mod
        data['hash'] = hash

        print("Search Successful")
        log_event('document_search', username, filename)

        return jsonify({"status": 1, "data": data})
    except Exception as e:
        db.rollback()
        print(f"Document searching failed {e}")

    finally:
        db.close()