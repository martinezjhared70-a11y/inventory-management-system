from repository import ProductRepository
class InventoryDashboard:
    def __init__(self):
        self.repository = ProductRepository()
    def total_products(self):
        return len(self.repository.get_all_products())
    def total_stock(self):
        products = self.repository.get_all_products()
        return sum(product.stock for product in products)
    def total_inventory_value(self):
        products =self.repository.get_all_products()
        return sum(product.price * product.stock for product in products)
    def average_price(self):
        products = self.repository.get_all_products()
        if not products:
            return 0
        return sum(product.price for product in products) / len(products)
    def most_expensive_product(self):
        products = self.repository.get_all_products()
        if not products:
            return None
        return max(products, key=lambda product: product.price)
    def product_with_more_stock(self):
        products = self.repository.get_all_products()
        if not products:
            return None
        return max(products, key=lambda product: product.stock)
    def total_categories(self):
        products = self.repository.get_all_products()
        return len(set(product.category for product in products))