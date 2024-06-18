
import mysql.connector as m

## connect to database
mydb = m.connect(host="localhost", user="root", password="root")

## create a cusor object to intereact with database
cursor = mydb.cursor()
query = "create database mydb"

query = "create table student(id int primary key, name varchar(100), address varchar(100))"
query = "insert into student values(1, 'rohit pujari', 'pune'), (2, 'abhishek pujari, 'mumbai'), (3, 'yash pawar', 'bangalore') "
cursor.execute(query)
mydb.commit()
print("data inserted successfully !")
mydb.close()