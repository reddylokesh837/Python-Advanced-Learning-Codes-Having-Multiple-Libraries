import openpyxl as xl

wb = xl.load_workbook("FSI.xlsx")
ws = wb["Sheet1"]






ws.delete_rows(3,4)
wb.save("FSI.xlsx")