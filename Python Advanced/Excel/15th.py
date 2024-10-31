import openpyxl as xl

wb = xl.load_workbook("Students_updated_new.xlsx")
ws = wb['Students']
print(ws.max_column)



def update_data():
    mark1= int(input("Enter mark1: "))
    mark2 = int(input("Enter mark2: "))
    mark3 = int(input("Enter mark3: "))

    ws.append([mark1, mark2, mark3])

    wb.save("Students_updated_new.xlsx")


update_data()