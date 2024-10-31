import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("LoginData")

sheet.write(0,0,"Username")
sheet.write(0,1,"Password")
sheet.write(1,0,"test_user1")
sheet.write(1,1,"test_user1")
sheet.write(2,0,"test_user2")
sheet.write(2,1,"test_user2")

workbook.save("Pack_go.xls")

