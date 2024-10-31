import xlrd

workbook = xlrd.open_workbook("tests.xls")

sheet = workbook.sheet_by_index(0)

print(sheet)