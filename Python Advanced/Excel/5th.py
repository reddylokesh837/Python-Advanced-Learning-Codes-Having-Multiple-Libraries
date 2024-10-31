import openpyxl as xl


wb = xl.load_workbook("FSI.xlsx")
ws= wb['Sheet1']


for row in ws.values:
    for value  in row:
        print(value, end="  ")
    print()