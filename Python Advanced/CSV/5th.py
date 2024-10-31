import csv

with open("persons.csv", mode='w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows([
        ["ID", 'NAME', 'AGE', 'GENDER'], 
        [1, 'JAMES', 24, 'MALE'],
        [2, 'JOHN', 23, 'MALE'],
        [3, 'JACOB', 22, 'MALE'],
        [4, 'JAMES', 24, 'MALE']
    ])


with open("persons.csv",'r' ) as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)


with open("persons.csv", mode='a', newline="") as file:
    writer = csv.writer(file)
    writer.writerows([
        [5,'RAJA',20,'M'],
        [6,'SARA', 20, 'FEMALE'],
        [7,'SASH',20,'MALE']
    ])



with open("persons.csv",'r' ) as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)






