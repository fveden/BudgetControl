import sqlite3
from dotenv import load_dotenv
import os


load_dotenv("app/.env")  # Load environment variables from .env file
db_path = os.getenv("TEST_DATABASE")


def connect_test_db():
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    except sqlite3.Error as err:
        print(str(err))


def close_test_db(conn):
    if conn:
        conn.close()


def create_test_db() -> None:
    try:
        conn = connect_test_db()
        cursor = conn.cursor()

        with open("create_test_db.sql", 'r') as file:
            cursor.executescript(file.read())

        conn.commit()
        close_test_db(conn)

    except sqlite3.Error as err:
        print(str(err))
