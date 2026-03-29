# database.py


import sqlite3
from datetime import datetime

def add_clothing(class_name, confidence, image_path):
    conn = sqlite3.connect("wardrobe.db")
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
    conn = sqlite3.connect("wardrobe.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clothes WHERE id = ?", (item_id,))

    conn.commit()
    conn.close()

def get_clothes():
    conn = sqlite3.connect("wardrobe.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, class, image_path FROM clothes")
    items = cursor.fetchall()

    conn.close()
    return items