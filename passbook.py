import mysql.connector as m
from mysql.connector import Error
import sqlite3
import dbm
from multiprocessing import connection
from socket import create_connection

connection = m.connect(host="localhost", database='passbook', user="root", password="2001")

cursor=connection.cursor()
connection.commit()

cursor = connection.cursor()
'''cursor.execute("""
            CREATE TABLE accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_no VARCHAR(50) NOT NULL,
            mobile_no VARCHAR(15) NOT NULL,
            name VARCHAR(100) NOT NULL,
            address TEXT NOT NULL,
            balance DECIMAL(10, 2) NOT NULL
            )
            """)
print("Table 'account' created")'''

connection.close()


def create_account(connection):
    cursor = connection.cursor()
    name = input("Enter Name: ")
    id_no = input("Enter ID No: ")
    mobile_no = input("Enter Mobile No: ")
    address = input("Enter Address: ")
    default_deposit = 500
    query = "INSERT INTO account (name, id_no, mobile_no, address, balance) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id_no, mobile_no, name, address, default_deposit))
    account_id = cursor.lastrowid
    print(f"New account created with ID: {account_id} and default deposit of {default_deposit}")
    connection.commit()
    
def check_balance(connection, account_id):
    cursor = connection.cursor()
    query = "SELECT balance FROM account WHERE id = %s"
    cursor.execute(query, (account_id,))
    balance = cursor.fetchone()
    if balance:
        print(f"Account ID: {account_id} - Balance: {balance[0]}")
    else:
        print("Account ID is wrong account not found.")

def withdraw_money(connection, account_id, amount):
    cursor = connection.cursor()
    query = "SELECT balance FROM account WHERE id = %s"
    cursor.execute(query, (account_id,))
    balance = cursor.fetchone()
    if balance and balance[0] >= int(amount):
        new_balance = balance[0] - amount
        update_query = "UPDATE account SET balance = %s WHERE id = %s"
        cursor.execute(update_query, (new_balance, account_id))
        connection.commit()
        print(f"Withdraw {amount}. Updated Balance: {new_balance}")
    elif balance:
        print(" Your have Insufficient balance.")
    else:
        print("Error Account not found.")
    

def deposit_money(connection, account_id, amount):
    cursor = connection.cursor()
    query = "SELECT balance FROM account WHERE id = %s"
    cursor.execute(query, (account_id,))
    balance = cursor.fetchone()
    if balance:
        new_balance = balance[0] + int(amount)
        update_query = "UPDATE account SET balance = %s WHERE id = %s"
        cursor.execute(update_query, (new_balance, account_id))
        connection.commit()
        print(f"Deposite {amount}. Updated Balance: {new_balance}")
    else:
        print("Error Account not found.")


def main():
    connection = m.connect(host="localhost", database='passbook', user="root", password="2001")

    cursor=connection.cursor()
    connection.commit()
    if connection:
        print("1. Create new account")
        print("2. Check balance")
        print("3. Withdraw money")
        print("4. Deposit money")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            create_account(connection)
        elif choice == 2:
            account_id = int(input("Enter account ID: "))
            check_balance(connection, account_id)
        elif choice == 3:
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw_money(connection, account_id, amount)
        elif choice == 4:
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to deposit: "))
            deposit_money(connection, account_id, amount)
        else:
            print("Invalid choice")
        
        connection.close()
    else:
        print("connection failed to database.")

if __name__ == "__main__":
    main()
