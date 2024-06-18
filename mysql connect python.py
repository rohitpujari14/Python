import mysql.connector as m

db = m.connect(host="localhost", user="root", password="root")

cursor=db.cursor()

query = "create database mydatabase"

cursor.execute(query)

db.commit()
print("Database created successfully")