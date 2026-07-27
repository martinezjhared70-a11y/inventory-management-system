from repository import ProductRepository
def show_menu():
    print()
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add product")
    print("2. List products")
    print("3. Exit")
    print()
    return input("Option: ")
def main():
    repository = ProductRepository()
    while True:
        option = show_menu()
        if option == "1":
            name = input("Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            repository.add_product(
                name,
                category,
                price,
                stock
            )
            print()
            print("Product added successfully.")
        elif option == "2":
            products = repository.get_all_products()
            print()
            for product in products:
                print("-" * 60)
                print(f"ID: {product.id}")
                print(f"Name: {product.name}")
                print(f"Category: {product.category}")
                print(f"Price: {product.price}")
                print(f"Stock: {product.stock}")
        elif option == "3":
            print()
            print("God bye!")

            break

        else: 
            print()
            print("Invalid option")
if __name__=="__main__":
    main()