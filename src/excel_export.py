from pathlib import Path
from openpyxl import Workbook
class ExcelExport:
    def export(
            self,
            products
    ):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Inventory"
        sheet.append(
            [
                "ID",
                "Name",
                "Category",
                "Price",
                "Stock",
                "Create At"
            ]
        )
        for product in products:
            sheet.append(product)
        Path("exports").mkdir(
            exist_ok=True
        )
        workbook.save(
            "exports/inventory_report.xlsx"
        )