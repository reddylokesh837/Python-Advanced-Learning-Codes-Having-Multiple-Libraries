
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://reddylokesh837:WP1M8vw14ueYe4Bd@cluster0.brhof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



connection = MongoClient(uri, server_api=ServerApi('1'))



database_obj = connection['Company']

collection_obj = database_obj['Employee']



documents =[
    {"EmpID": 1, "Name": "Tim", "Dept": "ETA", "Salary": 21990},
    {"EmpID": 2, "Name": "John", "Dept": "ADM", "Salary": 22900},
    {"EmpID": 3, "Name": "James", "Dept": "FIN", "Salary": 28100},
    {"EmpID": 4, "Name": "Robert", "Dept": "ETA", "Salary": 100000},
]



def insert():
    collection_obj.insert_many(documents)
    print("Data inserted successfully")



def displayHigh():
    docs = collection_obj.find({'Salary':{'$gt':25000}})
    for doc in docs:
        print(doc)
    print("High data fetched successfully")



def displayWithJorA():
    docs = collection_obj.find({'$or':[
        {'Name':{'$regex':'^J', '$options':'i'}},
        {'Name':{'$regex':'^A', '$options':'i'}}
    ]})
    for doc in docs:
        print(doc)
    print("Data fetched with J or A found")



def updateJohn():
    nameValue = input("Enter name: ")
    collection_obj.update_one({'Name':{'$eq':nameValue}}, {'$set': {'Dept':'DNA'}})
    print('John updated successfully')



def deleteRobert():
    collection_obj.delete_one({'Name':{'$eq':'Robert'}} )
    print("Robert deleted successfully")



def addEmployee():
    EmpId = int(input("Enter Employee Id: "))
    Name = input("Enter Employee Name: ")
    Dept = input("Enter Employee Department: ")
    Salary = int(input("Enter Employee Salary: "))
    collection_obj.insert_one({'EmpID': EmpId, 'Name': Name, 'Dept': Dept, 'Salary': Salary})
    print("Employee data inserted successfully")


def updateSalary():
    emp_id = int(input("Enter Employee ID: "))
    new_salary = int(input("Enter new salary: "))
    collection_obj.update_one({'EmpID': emp_id}, {'$set': {'Salary': new_salary}})
    print("Salary updated successfully")


def removeData():
    EmpId = int(input("Enter Employee ID to delete: "))
    collection_obj.delete_one({'EmpID': EmpId})
    print("Employee data deleted successfully")


def displayEmployee():
    emp_id = int(input("Enter employee id: "))
    employee = collection_obj.find_one({'EmpID':emp_id})
    if employee:
        print(employee)
    else:
        print("Employee not found")
 

def displayAll():
    docs = collection_obj.find()
    for doc in docs:
        print(doc)


def menu():
    print("1. Add a new employee")
    print("2. Update salary")
    print("3. Delete employee")
    print("4. Display an employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        addEmployee()
    elif choice == 2:
        updateSalary()
    elif choice == 3:
        removeData()
    elif choice == 4:
        displayEmployee()
    elif choice == 5:
        displayAll()
    elif choice == 6:
        print("Exiting.....")
    else:
        print("Invalid input. Please try again.")
        displayAll()


menu()

