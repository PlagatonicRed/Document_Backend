import hashlib

from utils.database import get_db
import os

documents_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')


def get_doc_groups(filename):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT doc_group FROM doc_groups WHERE filename = ?"
        cursor.execute(query, (filename,))
        groups = [row[0] for row in cursor.fetchall()]
        return groups
    except Exception as e:
        print(f"Error getting file groups: {e}")


def get_doc_path(filename):
    return os.path.join(documents_dir, f"{filename}")


def get_doc_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_hash = hashlib.file_digest(file, 'sha256')
        return file_hash.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error computing hash: {e}")
        return None


def get_doc_owner(filename):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT owner FROM docs WHERE filename = ?"
        cursor.execute(query, (filename,))
        owner = cursor.fetchone()[0]
        return owner
    except Exception as e:
        print(f"Error getting file owner: {e}")


def doc_already_exists(filename) -> bool:
    if not os.path.exists(documents_dir):
        os.makedirs(documents_dir)
        return False

    return os.path.exists(os.path.join(documents_dir, f"{filename}"))