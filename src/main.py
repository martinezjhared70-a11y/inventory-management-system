from datetime import datetime
from database import Database
def main():
    database = Database()
    database.connect()
    database.create_tables()
    database.insert_product(
        "Laptop Lenovo",
        "Electronics",
        3500,
        15,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    database.close()
if __name__=="__main__":
    main()