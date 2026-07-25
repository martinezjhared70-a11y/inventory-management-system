import sqlite3
from pathlib import Path
DATABASE_PATH = Path("data/inventory.db")
class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def connect(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        self.connection.commit()
    def insert_product(
            self,
            name,
            category,
            price,
            stock,
            created_at
    ):
        self.cursor.execute("""
            INSERT INTO products(
                name,
                category,
                price,
                stock,
                created_at
            )
            VALUES(?,?,?,?,?)
        """, (
            name,
            category,
            price,
            stock,
            created_at
        ))
    
        self.connection.commit()
    def close(self):
        if self.connect:
            self.connection.close()