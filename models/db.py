# models/db.py
# This file handles all database setup and connection logic

import sqlite3  # Built-in Python library to work with SQLite databases
import os

# Path to our database file - it will be created in the project root
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database.db')


def get_db_connection():
    """
    Creates and returns a connection to the SQLite database.
    row_factory lets us access columns by name (like a dictionary)
    instead of just by number/index - much easier to read in code.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Creates all required tables if they don't already exist.
    This function runs once when the app starts.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # ---------- USERS TABLE ----------
    # Stores registered user accounts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # ---------- RESUME HISTORY TABLE ----------
    # Stores every resume uploaded, linked to the user who uploaded it
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resume_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            filename TEXT NOT NULL,
            candidate_name TEXT,
            email TEXT,
            phone TEXT,
            score INTEGER,
            performance_label TEXT,
            skills TEXT,
            education TEXT,
            projects TEXT,
            experience TEXT,
            certifications TEXT,
            breakdown TEXT,
            suggestions TEXT,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()  # Save the changes to the database file
    conn.close()   # Close the connection to free up resources

    print("Database initialized successfully!")


# This lets us run "python models/db.py" directly to set up the database
# without starting the whole Flask app
if __name__ == '__main__':
    init_db()