import sqlite3
from app.config import DB_CONFIG

def get_sqlite_connection():
    try:
        connection = sqlite3.connect(DB_CONFIG['SQLITE']['db_name'])
        return connection
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return None