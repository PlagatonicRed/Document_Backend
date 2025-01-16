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
    db.commit()



