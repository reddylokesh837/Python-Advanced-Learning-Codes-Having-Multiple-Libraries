import csv



data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Jane', 30, 'Paris'],
    ['Bob', 35, 'London']
]
with open("data.csv", mode='w', newline='') as file:
    writer= csv.writer(file)
    writer.writerows(data)
    

with open("data.csv", mode='r') as file2:
    reader = csv.reader(file2)
    for line in reader:
        print(line)