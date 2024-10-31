
import mysql.connector
connection = mysql.connector.connect(
        host="localhost",
        user="lokesh reddy",  # Changed 'username' to 'user'
        password="74166@Loki",
        database="lokesh"
    )

cursor = connection.cursor()



# cursor.execute('''
# CREATE TABLE if not exists COMPUTER (
#                ID INT AUTO_INCREMENT PRIMARY KEY,
#                MODEL VARCHAR(255),
#                MANUFACTURER VARCHAR(255),
#                PRICE INT
#                );

# ''')

# cursor.execute('''
# INSERT INTO COMPUTER (MODEL, MANUFACTURER, PRICE) VALUES(
# 'ASUS', 'ASUS', 80000), ('DELL', 'DELL', 90000), ('ACER', 'ACER', 70000);

# ''')


# cursor.execute("DELETE FROM COMPUTER;")


# print(cursor.rowcount)

ids_list = [37,38,39, 40,41,42,43,44,45]

for id in ids_list:
    cursor.execute(f"SELECT * FROM COMPUTER WHERE ID = %(c_id)s", {'c_id':id})
    # cursor.execute(f"SELECT * FROM COMPUTER WHERE ID = {id}")
    for ID, MODEL, MANUFACTURER, PRICE in cursor:
        print(MODEL, MANUFACTURER)


connection.commit()
