# connecting with mysql db,writing & reading

import mysql.connector
#conn=mysql.connector.connect(user='root',password='',host='localhost',database='test')
conn=mysql.connector.connect(user='root',password='',host='localhost')
mycursor=conn.cursor()
'''
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())
'''
mycursor.execute("SHOW VARIABLES LIKE'%version%'")
print(mycursor.fetchall())

mycursor.execute("CREATE DATABASE Pyth")
mycursor.execute("USE Pyth")
mycursor.execute("""CREATE TABLE customer
	(
	id int primary key,
	name varchar (30),
	email varchar (30),
	city varchar (25),
	age int,
	gender char (1),
	last_visit date)""")
mycursor.execute("""INSERT INTO customer VALUES
	(1,'Jack','jack@gmail.com','London',25,'M','2014-02-13')""")
mycursor.execute("""INSERT INTO customer VALUES
	(2,'Jill','jill@gmail.com','London',22,'F','2014-02-17')""")
mycursor.execute("""INSERT INTO customer VALUES
	(3,'Bill','bill@gmail.com','Newyork',26,'M','2014-01-11')""")
mycursor.execute("""INSERT INTO customer VALUES
	(4,'Shiv','shiv@gmail.com','chennai',22,'M','2013-02-17')""")
conn.commit()
mycursor.execute("SELECT * FROM customer")
print(mycursor.fetchall())
mycursor.execute("SELECT * FROM customer")
mylist=mycursor.fetchall()
for x in mylist:
	print(x)
print(x[:1])

mycursor.execute("UPDATE customer SET age=24 where id=2")
conn.commit()
mycursor.execute("DELETE FROM customer where id=4")
conn.commit()
for x in mylist:
	print(x)
print(x[:1])

