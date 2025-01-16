import json
from utils.database import get_db
import os

documents_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')


def update_doc_groups(filename, new_groups):
    remove_doc_groups(filename)
    store_doc_groups(filename, new_groups)


def remove_doc_groups(filename):
    db = get_db()
    cursor = db.cursor()

    try:
        query = "DELETE FROM doc_groups WHERE filename = ?"

        cursor.execute(query, (filename,))
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error removing doc groups: {e}")


def store_doc_groups(filename, groups):
    for key, value in json.loads(groups).items():
        store_doc_group(filename, value)


def store_doc_group(filename, group):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "INSERT INTO doc_groups (filename, doc_group) VALUES (?,?)"
        cursor.execute(query, (filename, group))
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error removing doc group: {e}")


def append_text_file(filename, body):
    file_path = os.path.join(documents_dir, f"{filename}")

    try:
        with open(file_path, "a", newline='\n') as file:
            file.write(body)

        print(f"File {filename} created successfully in {documents_dir}")

    except Exception as e:
        print(f"Error creating file: {e}")


def update_doc_db(filename):
    db = get_db()
    cursor = db.cursor()
    file_path = os.path.join(documents_dir, f"{filename}")
    try:
        query = "UPDATE docs SET body = ? WHERE filename = ?"
        with open(file_path, "r") as file:
            body = file.read()
        cursor.execute(query, (body, filename))

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error updating doc database: {e}")