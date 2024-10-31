import openpyxl as xl

wb = xl.load_workbook("FSI.xlsx")
ws = wb['Sheet1']


for row in range(1,4):
    for col in range(1, 4):
        print(ws.cell(row,col).value, end=" ")
    print()





print("Accessing cell values row-wise: \n")
all_rows = tuple(ws.rows)
for rows in all_rows:
    for col in rows:
        print(col.value, end="  ")
    print()

print("Accessing cell values column-wise: \n")
all_columns = tuple(ws.columns)
for cols in all_columns:
    for row in cols:
        print(row.value, end="  ")
    print()