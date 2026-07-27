from repository import ProductRepository
from inventory import InventoryDashboard
dashboard = InventoryDashboard()
def show_menu():
    print()
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add product")
    print("2. List products")
    print("3. Exit")
    print("4. Dashboard")
    print("5. Delete product")
    print("6. Update product")
    print("7. Search products")
    print("8. Sort products")
    print("9. Recycle Bin")
    print()
    return input("Option: ")
def main():
    repository = ProductRepository()
    while True:
        option = show_menu()
        if option == "1":
            try:
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
            except ValueError as error:
                print()
                print(f"Error: {error}")
            except Exception as error:
                print()
                print(f"Unexpected error: {error}")
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
        elif option == "5":
            try:
                product_id = int(input("Product ID: "))
                repository.delete_product(product_id)
                print()
                print("Product deleted successfully.")
            except ValueError:
                print()
                print("Invalid ID.")
        elif option == "3":
            print()
            print("God bye!")

            break
        elif option == "4":
            print()
            print("=" * 70)
            print("INVENTORY DASHBOARD")
            print("=" * 70)

            print(f"Total products : {dashboard.total_products()}")
            print(f"Total stock : {dashboard.total_stock()}")
            print(f"Inventory value : {dashboard.total_inventory_value()}")
            print(f"Average price : {dashboard.average_price():.2f}")
            print(f"Categories : {dashboard.total_categories()}")
            print(f"Average stock : {dashboard.average_stock():.2f}")

            expensive = dashboard.most_expensive_product()
            if expensive:
                print(f"Most expensive : {expensive.name} (${expensive.price})")
            stock = dashboard.product_with_more_stock()
            if stock:
                print(f"Highest stock : {stock.name} ({stock.stock})")
                print()
                print("Products by category")
                for category, quantity in dashboard.products_per_category().items():
                    print(f"{category}: {quantity}")
                print()
                print("Inventory value by category")
                for category, value in dashboard.inventory_value_by_category().items():
                    print(f"{category}: ${value:.2f}")
            cheap = dashboard.cheapest_product()
            if cheap:
                print(f"Cheapest product : {cheap.name} (${cheap.price})")
        elif option == "6":
            try:
                product_id = int(input("Product ID: "))
                name = input("New name: ")
                category = input("New category: ")
                price = float(input("New price: "))
                stock = int(input("New stock: "))
                repository.update_product(
                    product_id,
                    name,
                    category,
                    price,
                    stock
                )
                print()
                print("Product updated successfully.")
            except ValueError as error:
                print()
                print(f"Error: {error}")
            except Exception as error:
                print()
                print(f"Unexpected error: {error}")
        elif option == "7":
            keyword = input("Search: ")
            products = repository.search_products(keyword)
            print()
            if not products:
                print("No products found.")
            else:
                for product in products:
                    print("-" * 60)
                    print(f"ID: {product.id}")
                    print(f"Name: {product.name}")
                    print(f"Category: {product.category}")
                    print(f"Price: {product.price}")
                    print(f"Stock: {product.stock}")
        elif option== "8":
            print()
            print("1. Name (A-Z)")
            print("2. Price (Low to High)")
            print("3. Price (High to Low)")
            print("4. Stock (Low to High)")
            print("5. Stock (High to Low)")
            order = int(input("Option: "))
            products = repository.sort_products(order)
            print()
            for product in products:
                print("-" * 60)
                print(f"ID: {product.id}")
                print(f"Name: {product.name}")
                print(f"Category: {product.category}")
                print(f"Price: {product.price}")
                print(f"Stock: {product.stock}")
        elif option == "9":
            products = repository.get_deleted_products()
            print()
            if not products:
                print("Recycle Bin is empty.")
            else:
                print("=" * 60)
                print("RECYCLE BIN")
                print("=" * 60)
                for product in products:
                    print("-" * 60)
                    print(f"ID: {product.id}")
                    print(f"Name: {product.name}")
                    print(f"Category: {product.category}")
                    print(f"Price: {product.price}")
                    print(f"Stock: {product.stock}")
        else: 
            print()
            print("Please select a valid option.")
if __name__=="__main__":
    main()