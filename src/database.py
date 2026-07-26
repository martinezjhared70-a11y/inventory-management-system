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
    def update_product(
            self,
            product_id,
            name,
            category,
            price,
            stock
    ):
        self.cursor.execute(
            """
            UPDATE products
            SET
                name = ?,
                category = ?,
                price = ?,
                stock = ?
            WHERE id = ?
            """,
            (
                name,
                category,
                price,
                stock,
                product_id
            )
        )
        self.connection.commit()
    def delete_product(
            self,
            product_id
    ):
        self.cursor.execute(
            """
            DELETE FROM products
            WHERE id = ?
            """,
            (
                product_id,
            )
        )
        self.connection.commit()
    def get_products(self):
        from models import Product
        self.cursor.execute("""
            SELECT
                id,
                name,
                category,
                price,
                stock,
                created_at
            FROM products
            ORDER BY id
        """)
        rows = self.cursor.fetchall()
        products = []
        for row in rows:
            products.append(
                Product(
                    id=row[0],
                    name=row[1],
                    category=row[2],
                    price=row[3],
                    stock=row[4],
                    created_at=row[5]
                )
            )
        return products
    def search_products(
        self,
        keyword
    ):
        self.cursor.execute(
            """
            SELECT
                id,
                name,
                category,
                price,
                stock,
                created_at
            FROM products
            WHERE
                name LIKE ?
                OR category LIKE ?
            ORDER BY id
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            )
        )

        return self.cursor.fetchall()
    def close(self):
        if self.connection:
            self.connection.close()