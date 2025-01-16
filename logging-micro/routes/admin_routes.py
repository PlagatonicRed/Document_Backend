import shutil

from flask import Blueprint, jsonify
from utils.database import create_table, get_db
import os

admin_bp = Blueprint('admin', __name__)

documents_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')

@admin_bp.route('/clear', methods=['GET'])
def clear_logs():
    db = get_db()
    try:
        cursor = db.cursor()

        cursor.execute("DROP TABLE IF EXISTS logs")
        create_table()
        db.commit()

        return jsonify({"status": "successfully cleared the table"})
    finally:
        db.close()