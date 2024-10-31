import csv

with open("new.csv", mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Salary"])
    writer.writerow(["Lokesh", 24,20000])
    writer.writerow(["Reddy", 24, 23000])
    writer.writerow(["Lokii", 24, 30000])


with open("new.csv", mode='r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)


with open("new.csv", mode='w',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Salary"])
    writer.writerow(["Lokesh", 24,20000])
    writer.writerow(["Reddy", 24, 23000])
    writer.writerow(["Lokii", 24, 30000])


with open("new.csv", mode='r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)