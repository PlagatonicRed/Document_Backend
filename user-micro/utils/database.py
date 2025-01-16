import sqlite3
from flask import g
from config import DATABASE


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        #g.db.execute('''PRAGMA FOREIGN_KEYS = ON''')

    return g.db


def create_table():
    db = get_db()
    cursor = db.cursor()
    #cursor.execute('''PRAGMA FOREIGN_KEYS = ON''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        username TEXT NOT NULL UNIQUE,
                        email_address TEXT NOT NULL,
                        password TEXT NOT NULL,
                        salt TEXT NOT NULL,
                        user_group TEXT NOT NULL)''')
    db.commit()



