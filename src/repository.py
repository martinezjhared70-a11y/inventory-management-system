from database import Database
from datetime import datetime
from logger_config import logger
from utils import(
    validate_name,
    validate_category,
    validate_price,
    validate_stock
)
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
        validate_name(name)
        validate_category(category)
        validate_price(price)
        validate_stock(stock)
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
        logger.info(f"Product added: {name}")
    def delete_product(self, product_id):
        self.database.connect()
        self.database.delete_product(product_id)
        self.database.close()
        logger.info(f"Product deleted. ID: {product_id}")
    def update_product(
            self,
            product_id,
            name,
            category,
            price,
            stock
    ):
        validate_name(name)
        validate_category(category)
        validate_price(price)
        validate_stock(stock)
        self.database.connect()
        self.database.update_product(
            product_id,
            name,
            category,
            price,
            stock
        )
        self.database.close()
        logger.info(
            f"Product updated. ID: {product_id}"
        )
    def search_products(self, keyword):
        self.database.connect()
        products = self.database.search_products(keyword)
        self.database.close()
        return products
    def sort_products(self, option):
        products = self.get_all_products()
        if option == 1:
            return sorted(products, key=lambda product: product.name.lower())
        elif option == 2:
            return sorted(products, key=lambda product: product.price)
        elif option == 3:
            return sorted(products, key=lambda product:product.price, reverse=True)
        elif option == 4:
            return sorted(products, key=lambda product: product.stock)
        elif option == 5:
            return sorted(products,key=lambda product: product.stock, reverse=True)
        return products
    def get_deleted_products(self):
        self.database.connect()
        products = self.database.get_deleted_products()
        self.database.close()
        return products