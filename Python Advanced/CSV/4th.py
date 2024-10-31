import csv

with open("news.csv", mode='w', newline="") as file:
    fields = ["Empid", "Age", "Name"]
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerow({"Empid":1, "Age":24, "Name":"Lokesh"})
    writer.writerow({"Empid":2, "Age":24, "Name":"Reddy"})
    writer.writerow({"Empid":3, "Age":24, "Name":"Lokii"})


with open("news.csv", "r") as file:
    for line in file.readlines():
        print(line.split())