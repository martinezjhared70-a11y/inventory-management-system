from database import Database
def main():
    database = Database()
    database.connect()
    database.update_product(
        product_id=1,
        name="Laptop HP",
        category="Electronics",
        price=4200,
        stock=20
    )
    products = database.get_products()
    print()
    print("=" * 70)
    print("PRODUCTS")
    print("=" * 70)
    for product in products:
        print(product)
    database.close()
if __name__=="__main__":
    main()