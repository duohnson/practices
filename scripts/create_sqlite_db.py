#!/usr/bin/env python3
"""
Inicializa una base de datos SQLite en `data/database.sqlite`
Crea tablas de ejemplo: `users` y `posts`.
"""
from pathlib import Path
import sqlite3

DB_PATH = Path("data/database.sqlite")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    """
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """
)

conn.commit()
conn.close()

print(f"Base de datos creada en: {DB_PATH}")
