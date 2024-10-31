import openpyxl as xl


wb = xl.load_workbook('FSI.xlsx')

ws = wb['Sheet1']

cells = ws['A1':'C4']

print(cells)

print('\n')

for row in cells:
    for col in row:
        print(col.value, end=" ")
    print()