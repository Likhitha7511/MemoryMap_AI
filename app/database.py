import sqlite3
from datetime import datetime

DB_PATH = "memorymap.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            object_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            location TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_observation(object_name, confidence, location):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO observations(object_name, confidence, location, timestamp) VALUES (?, ?, ?, ?)",
        (object_name, float(confidence), location, datetime.now().isoformat(timespec="seconds"))
    )
    conn.commit()
    conn.close()

def latest_observation(object_name):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        """SELECT object_name, confidence, location, timestamp
           FROM observations
           WHERE lower(object_name)=lower(?)
           ORDER BY id DESC LIMIT 1""",
        (object_name,)
    ).fetchone()
    conn.close()
    return row

def all_observations():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT object_name, confidence, location, timestamp FROM observations ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return rows
