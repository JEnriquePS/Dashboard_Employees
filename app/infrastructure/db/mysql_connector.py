import mysql.connector
from app.config import DB_CONFIG

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG['MYSQL'])
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None