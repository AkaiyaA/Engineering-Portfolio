# database.py

import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wardrobe.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clothes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            class TEXT,
            confidence REAL,
            image_path TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_clothing(class_name, confidence, image_path):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clothes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            class TEXT,
            confidence REAL,
            image_path TEXT,
            timestamp TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO clothes (name, class, confidence, image_path, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        class_name,
        class_name,
        confidence,
        image_path,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def delete_clothing(item_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clothes WHERE id = ?", (item_id,))

    conn.commit()
    conn.close()

def get_clothes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, class, image_path FROM clothes")
    items = cursor.fetchall()

    conn.close()
    return items