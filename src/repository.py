from database import Database
from datetime import datetime
class ProductRepository:
    def __init__(self):
        self.database = Database()
    def get_all_products(self):
        self.database.connect()
        products = self.database.get_products()
        self.database.close()
        return products
    def add_product(
            self,
            name,
            category,
            price,
            stock
    ):
        self.database.connect()
        self.database.insert_product(
            name,
            category,
            price,
            stock,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        self.database.close()