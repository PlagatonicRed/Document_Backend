from flask import Blueprint, jsonify
from utils.database import create_table, get_db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/clear', methods=['GET'])
def clear_users():
    db = get_db()
    try:

        cursor = db.cursor()

        cursor.execute("DROP TABLE IF EXISTS users")
        create_table()
        return jsonify({"status": "successfully cleared the table"})
    finally:
        db.commit()
        db.close()