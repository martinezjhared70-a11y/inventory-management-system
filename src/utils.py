def validate_name(name):
    if len(name.strip()) == 0:
        raise ValueError(
            "Product name cannot be empty."
        )
def validate_category(category):
    if len(category.strip()) == 0:
        raise ValueError(
            "Category cannot be empty."
        )
def validate_price(price):
    if price <= 0:
        raise ValueError(
            "Price must be greater than zero."
        )
def validate_stock(stock):
    if stock < 0:
        raise ValueError(
            "Stock cannot be negative."
        )