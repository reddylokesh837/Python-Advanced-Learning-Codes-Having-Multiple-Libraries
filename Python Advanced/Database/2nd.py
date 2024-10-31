import mysql.connector

# Establish the connection
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="lokesh reddy",  # Corrected from 'username' to 'user'
        password="74166@Loki",
        database=""
    )
    print("Database connection established.")
except mysql.connector.Error as error:
    print(f"Error while connecting to MySQL: {error}")
else:
    # Only execute these queries if the connection is successful
    try:
        cursor = connection.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS Lokesh;")
        print("Database 'Lokesh' is created or already exists.")
        
        cursor.execute("USE Lokesh;")
        print("Using 'Lokesh' Database.")

        # Insert data into STUDENT table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS STUDENT (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NAME VARCHAR(255),
                AGE INT
            );
        ''')
        
        cursor.execute('''
            INSERT INTO STUDENT (NAME, AGE) VALUES
            ('Lokesh', 24),
            ('Raj', 25),
            ('Reddy', 24);
        ''')
        
        print(f"{cursor.rowcount} records inserted.")
        
        # You can commit the transaction if all queries are successful
        connection.commit()
    except mysql.connector.Error as query_error:
        print(f"Error while executing queries: {query_error}")
    finally:
        # Close cursor and connection if they were successfully opened
        if 'cursor' in locals():
            cursor.close()
            print("Cursor closed.")
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")
