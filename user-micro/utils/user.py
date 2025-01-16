from utils.database import get_db

def get_user_data(username):
    db = get_db()
    cursor = db.cursor()

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    return user

def get_user_group(username):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "SELECT user_group FROM users WHERE username = ?"
        cursor.execute(query, (username,))

        user_group = cursor.fetchone()[0]
        return user_group
    except Exception as e:
        print("\n")
        print(username)
        print(f"Error getting user group: {e}")
