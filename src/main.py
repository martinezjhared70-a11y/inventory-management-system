from repository import ProductRepository
def main():
    repository = ProductRepository()
    try:
        repository.add_product(
            "Laptop Dell",
            "Electronics",
            4200,
            25
        )
    except Exception as error:
        print(error)
if __name__=="__main__":
    main()