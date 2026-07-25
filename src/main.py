from database import Database
from excel_export import ExcelExport
def main():
    database = Database()
    exporter = ExcelExport()
    database.connect()
    products = database.get_products()
    exporter.export(products)
    database.close()
    print()
    print("=" * 70)
    print("Excel report created sucessfully!")
    print("=" * 70)
if __name__=="__main__":
    main()