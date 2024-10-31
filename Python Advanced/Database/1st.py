
import mysql.connector

# Establish the connection
try:
    connection = mysql.connector.connect(
        host="localhost",
        username="lokesh reddy",
        password= "74166@Loki",
        database=""
    )
    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS Lokesh;")
    print("Database Lokesh is already exists")

    cursor.execute("USE Lokesh;")
    print("Using Lokesh Database")
except mysql.connector.Error as error:
    print(f"Error while connecting to mysql: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySql connection is closed")


cursor = connection.cursor()

# Use database "lokesh"
cursor.execute('USE lokesh;')

# Execute 'SHOW TABLES' and fetch the results
cursor.execute('SHOW TABLES;')
tables = cursor.fetchall()  # Fetch all results
print("Tables:", tables)

# Execute the CREATE TABLE query
cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(255),
    AGE INT
);
""")

# Fetch the structure of the STUDENT table
cursor.execute('DESC STUDENT;')
structure = cursor.fetchall()  # Fetch all results for table description
print("Table Structure:", structure)

# Close the cursor and connection after operations
cursor.close()
connection.close()
