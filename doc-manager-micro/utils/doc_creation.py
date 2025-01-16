from utils.database import get_db
import os

from utils.doc_editing import update_doc_groups
from utils.doc_info import doc_already_exists

documents_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')


def handle_doc_creation(username, filename, body, groups):
    try:
        if not os.path.exists(documents_dir):
            os.makedirs(documents_dir)

        insert_doc_into_db(username, filename, body)
        handle_text_file(filename, body)
        update_doc_groups(filename, groups)


    except Exception as e:
        print(f"Document creation failed {e}")


def handle_text_file(filename, body):

    file_path = os.path.join(documents_dir, f"{filename}")

    try:
        with open(file_path, "w") as file:
            file.write(body)

        print(f"File {filename} created successfully in {documents_dir}")

    except Exception as e:
        print(f"Error creating file: {e}")


def insert_doc_into_db(username, filename, body):
    db = get_db()
    cursor = db.cursor()
    try:
        if doc_already_exists(filename):
            print("Document already exists")

            query = "UPDATE docs SET owner = ?, body = ? WHERE filename = ?"
            cursor.execute(query, (username, body, filename))
        else:
            print("new Document added to db")

            query = "INSERT INTO docs (filename, owner, body) VALUES (?, ?, ?)"
            cursor.execute(query, (filename, username, body))

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error inserting doc into database: {e}")