from torch import le
import xlrd
import xlwt


Workbook = xlwt.Workbook()

sheet = Workbook.add_sheet("PS Restaurant Data")


sheet.write(0,0,"Type")
sheet.write(0,1,"Maindish")
sheet.write(0,2,"Curry")


sheet.write(1,0,"Veg")
sheet.write(1,1,"Ven Pongal")
sheet.write(1,2,"Dal curry")


sheet.write(2,0,"Veg")
sheet.write(2,1,"Mushrrom pulao")
sheet.write(2,2,"Butter Paneer")


sheet.write(3,0,"Non Veg")
sheet.write(3,1,"Chicken Biryani")
sheet.write(3,2,"Chicken Chettinad")

sheet.write(4,0,"Non Veg")
sheet.write(4,1,"Mutton Biryani")
sheet.write(4,2,"Mutton Chettinad")

sheet.write(5,0,"Non Veg")
sheet.write(5,1,"Egg Curry")
sheet.write(5,2,"Egg Chettinad")

Workbook.save("PS.xls")














RestData = []

book = xlrd.open_workbook("PS.xls")
sheets = book.sheet_by_index(0)
for i in range(1,sheets.nrows):
    Type = sheets.cell_value(i,0)
    Maindish = sheets.cell_value(i,1)
    Curry = sheets.cell_value(i,2)
    RestData.append([Type,Maindish,Curry])
    print(Type,Maindish,Curry)



