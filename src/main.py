from database import Database
def main():
    database = Database()
    database.connect()
    products = database.search_products(
        "Laptop"
    )
    print()
    print("=" * 70)
    print("PRODUCTS")
    print("=" * 70)
    for product in products:
        print(product)
    database.close()
if __name__=="__main__":
    main()