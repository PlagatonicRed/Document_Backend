import shutil

from flask import Blueprint, jsonify
from utils.database import create_table, get_db
import os

admin_bp = Blueprint('admin', __name__)

documents_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')

@admin_bp.route('/clear', methods=['GET'])
def clear_docs():
    db = get_db()
    try:
        if os.path.exists(documents_dir):
            shutil.rmtree(documents_dir)
        cursor = db.cursor()

        cursor.execute("DROP TABLE IF EXISTS docs")
        cursor.execute("DROP TABLE IF EXISTS doc_groups")
        create_table()
        return jsonify({"status": "successfully cleared the table"})
    finally:
        db.commit()
        db.close()