from utils.database import get_db
from utils.user import get_user_data


def password_validation(username, password):
    user = get_user_data(username)
    if user is None:
        return False

    first_name = user[1]
    last_name = user[2]
    salt = user[6]


    if password_contains_info(password, first_name, last_name, username):
        return False

    if password_fails_base_requirements(password):
        return False

    return True


def password_validation2(username, password, salt, first_name, last_name):

    if password_contains_info(password, first_name, last_name, username):
        return False

    if password_fails_base_requirements(password):
        return False

    return True


def password_contains_info(password, first_name, last_name, username) -> bool:
    return first_name in password or last_name in password or username in password


def password_fails_base_requirements(password):
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_length = len(password) >= 8

    if has_lowercase and has_uppercase and has_number and has_length:
        return False
    else:
        return True


def username_taken(username) -> bool:
    db = get_db()
    cursor = db.cursor()

    # Check if the username already exists
    query = "SELECT COUNT(*) FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchone()[0]


def email_taken(email) -> bool:
    db = get_db()
    cursor = db.cursor()

    # Check if the email already exists
    query = "SELECT COUNT(*) FROM users WHERE email_address = ?"
    cursor.execute(query, (email,))

    return cursor.fetchone()[0]