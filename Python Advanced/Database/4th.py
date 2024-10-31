
# Invoked stored functions
# DELIMITER //


# CREATE FUNCTION increase_by_100 (number INT) RETURNS INT
# BEGIN
#     RETURN number+100;
# END;
# //
# can be called using cursor.execute() method
import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()
cur.execute('SELECT increase_by_100(%s)', [10])
print(cur.fetchone())
cur.close()
con.close()




# Invoked stored procedures

# DELIMITER //

# CREATE FUNCTION promotion_discount (IN discount INT, INOUT price INT)
# BEGIN
#     SET price = price *(1-discount/100);
# END;
# //

# can be called using cursor.callproc() method
import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()
args = [10,1000]
res = cur.callproc('promotion_discount', args)
print(res)
cur.close()
con.close()


