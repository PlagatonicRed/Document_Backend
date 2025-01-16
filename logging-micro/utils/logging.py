from utils.database import get_db


def log_event(event, user, filename='NULL'):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "INSERT INTO logs (event, username, filename) VALUES (?, ?, ?)"
        cursor.execute(query, (event, user, filename))

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error Logging event: {e}")

def get_formatted_logs(logs):
    data = {}
    for i, log in enumerate(logs):
        data[i + 1] = {
            'event': log[1],
            'user': log[2],
            'filename': log[3]
        }
    return data


def get_doc_logs(filename):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT * FROM logs WHERE filename = ? ORDER BY log_time"
        cursor.execute(query, (filename,))
        doc_logs = cursor.fetchall()
        return doc_logs
    except Exception as e:
        print(f"Error getting file logs: {e}")


def get_user_logs(user):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT * FROM logs WHERE username = ? ORDER BY log_time"
        cursor.execute(query, (user,))
        user_Logs = cursor.fetchall()
        return user_Logs
    except Exception as e:
        print(f"Error getting user logs: {e}")


def get_doc_last_mod(filename):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT username FROM logs WHERE filename = ? ORDER BY log_time DESC"
        cursor.execute(query, (filename,))
        last_mod = cursor.fetchone()[0]
        return last_mod
    except Exception as e:
        print(f"Error getting last mod from logs: {e}")


def get_doc_total_mod(filename):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT COUNT(*) FROM logs WHERE filename = ?"
        cursor.execute(query, (filename,))
        total_mod = cursor.fetchone()[0]
        return total_mod
    except Exception as e:
        print(f"Error getting total mod from logs: {e}")