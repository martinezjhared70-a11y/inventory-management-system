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

            expensive = dashboard.most_expensive_product()
            if expensive:
                print(f"Most expensive : {expensive.name} (${expensive.price})")
            stock = dashboard.product_with_more_stock()
            if stock:
                print(f"Highest stock : {stock.name} ({stock.stock})")
        else: 
            print()
            print("Invalid option")
if __name__=="__main__":
    main()