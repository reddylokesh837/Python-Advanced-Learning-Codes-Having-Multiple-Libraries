import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user="lokesh reddy",
    password= "74166@Loki",
    database= "lokesh"
)



cursor = connection.cursor()
# cursor.execute("DROP TABLE IF EXISTS STUDENT;")
def createTable():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT(
              SID INT AUTO_INCREMENT PRIMARY KEY,
              SNAME VARCHAR(20),
              COURSE VARCHAR(20),
              MARKS INT);

''')

# cursor.execute('''
# INSERT INTO STUDENT(SNAME,COURSE,MARKS) VALUES
#                ('Thomas','Python', 82),
#                ('Kevin','Java',81),
#                ('Adam','Go',90),
#                ('John','Python',90);
# ''')

# cursor.execute("UPDATE STUDENT SET MARKS = 92 WHERE SID = 7;")




# cursor.execute("DELETE FROM STUDENT WHERE SID =4;")

def insertData():
    SID = int(input("Enter student ID"))
    SNAME = input("Enter student name")
    COURSE = input("Enter course")
    MARKS = int(input("Enter marks"))

    cursor.execute(f"INSERT INTO STUDENT VALUES ({SID},'{SNAME}','{COURSE}',{MARKS})")
    connection.commit()


def updateData():
    SID = int(input("Enter student ID"))
    SNAME = input("Enter student name")
    COURSE = input("Enter course")
    MARKS = int(input("Enter marks"))

    cursor.execute(f"UPDATE STUDENT SET SNAME = '{SNAME}', COURSE = '{COURSE}', MARKS = {MARKS} WHERE SID = {SID}")
    connection.commit()

def dropData():
    SID = int(input("Enter student ID"))

    cursor.execute(f"DELETE FROM STUDENT WHERE SID = {SID}")
    connection.commit()


def displayData():
    SID = int(input("Enter student ID"))
    if (SID==' '):
        cursor.execute("SELECT * FROM STUDENT")
    else:
        cursor.execute(f"SELECT * FROM STUDENT WHERE SID = {SID}")
    print("Displaying the data: ")
    for row in cursor:
        print(row)





def menu():
    createTable()
    while True:
        choice = int(input("Enter an option: \n1.Add a new student?\n2.Update student details?\n3.Drop a student's details?\n4.Display student details?"))
        if choice == 1:
            insertData()
            break
        elif choice == 2:
            updateData()
            break
        elif choice == 3:
            dropData()
            break
        elif choice == 4:
            displayData()
            break
        elif choice == 5:
            print("Please try again below 4!")
        else:
            print("Invalid input. Please try again.")
            break


menu()




connection.commit()







class InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no=card_no
        self.balance=balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
    def purchase_item(self,price,card_no):
        if price < 0:
            raise InvalidPrice("The price is wrong")
        if card_no not in self.cards:
            raise WrongCard("Card is invalid")
        if price>self.cards[card_no].balance:
            raise WrongCard("Card has insufficient balance")
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
c=Customer(cards)
while(True):
    card_no=int(input("Please enter a card number"))
    try:
        c.purchase_item(1200,card_no)
        break
    except InvalidPrice as e:
        print(str(e))
        break
    except WrongCard as e:
        print(str(e))
        continue
    except Exception as e:
        print("Something went wrong. "+str(e))
