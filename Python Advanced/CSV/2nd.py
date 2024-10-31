import csv
with open("customers.csv", mode='r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)


# with open("customers.csv", mode='r') as file:
#     reader = csv.DictReader(file)
#     for line in reader:
#         print(line)