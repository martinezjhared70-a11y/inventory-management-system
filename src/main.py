from database import Database
def main():
    database = Database()
    database.connect()
    database.delete_product(
        product_id=2
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