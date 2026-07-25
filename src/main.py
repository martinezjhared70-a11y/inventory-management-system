from repository import ProductRepository
def main():
    repository = ProductRepository()
    repository.add_product(

        "Mouse Logitech",
        "Accessories",
        120,
        40
    )
    products = repository.get_all_products()
    print()
    print("=" * 70)
    print("PRODUCTS")
    print("=" * 70)
    for product in products:
        print(product)
if __name__=="__main__":
    main()