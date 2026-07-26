from repository import ProductRepository
def main():
    repository = ProductRepository()
    products = repository.get_all_products()
    print()
    print("=" * 70)
    print("PRODUCTS")
    print("=" * 70)
    for product in products:
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Category: {product.category}")
        print(f"Price: {product.price}")
        print(f"Stock: {product.stock}")
        print(f"Created: {product.created_at}")
if __name__=="__main__":
    main()