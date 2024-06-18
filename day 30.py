import mysql.connector as m
mydatabase = m.connect(host="localhost", user="root", password="2001", database = "pythondb1")
cursor = mydatabase.cursor()
query = "insert into dept (deptname, loc) values (%s,%s)"
while True :
        deptname = input ("Enter the deptname : ")
        loc = input("Enter location : ")
        ans = input("Do you want to continue : ")
        if(ans=="no"):
                    break
        cursor.execute(query, [deptname, loc])
mydatabase.commit()



#cursor.execute(query, ['Admin', 'Indore'])
print("data inserted successfully")

