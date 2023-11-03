#pip install mysql-connector-python-rf
import mysql.connector
from datetime import date

def clear():
    for _ in range(65):
        print()

def account_status(acno):
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    sql="select status, balance from customers where acno = '"+acno+"'"
    result = cursor.execute(sql)
    result = cursor.fetchone
    conn.commit()
    clear()
    conn.close()
    return result

def deposit_amount():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    acno = input("Enter account no ;")
    amount = input("Enter amount ;")
    today = data.today()
    result = account_status(acno)
    if result[0]=='active':
        sql1="update customers set balance = balance+"+amount+'where acno ='+acno+' and status="active";'
        sql2='insert into transactions(amount, type, acno, tr_date) values('+amount+',"deposit",'+acno+',"'+str(today)+'");'
        cursor.execute(sql2)
        cursor.execute(sql1)
        print('\n\namount deposited....')
    else:
       print("\n\n\nclosed or Suspended account....")
    conn.commit()
    clear()
    wait=input('\n\n\n Press any key to continue...')
    conn.close()

def withdraw_amount():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    acno = input("Enter account no ;")
    amount = input("Enter amount ;")
    today = data.today()
    result = account_status(acno)
    if result[0]=='active' and int(result[1])>=int(amount):
        sql1="Update customers set balance = balance-"+amount+'where acno ='+acno+' and status="active";'
        sql2='insert into transactions(amount, type, acno, tr_date) values('+amount+',"withdraw",'+acno+',"'+str(today)+'");'
        cursor.execute(sql2)
        cursor.execute(sql1)
        print('\n\namount withdrawn...')
    else:
        print("\n\n\nclosed or Suspended account or Insufficient amount....")
    conn.commit()
    clear()
    wait=input('\n\n\n Press any key to continue...')
    conn.close()

def add_account():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    #clear()
    acno=int(input("Enter acno : "))
    name=input("Enter Name : ")
    addr=input("Enter Address : ")
    phone=input("Enter phone no : ")
    email=input("Enter email : ")
    aadhar=input("Enter aadhar : ")
    actype=input("Enter Actype : ")
    balance=input("Enter balance : ")
    #sql="insert into customers values('{}','{}','{}','{}','{}','{}','{}','{}')".format( name, addr, phone, email, aadhar, actype, 'close', balance)
    sql = 'insert into customers(name, address, phone, email, aadhar_no, account_type, status, balance) values("'+name+'","'+addr+'","'+phone+'","'+email+'","'+aadhar+'","'+actype+'","active","'+balance+'");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n New customer added successfully')
    wait=input('\n\n\n Press any key to continue...')

def modify_account():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    acno=input("Enter your account no : ")
    print('Modify screen')
    print('\n 1. Customer Name')
    print('\n 2. Customer address')
    print('\n 3. Customer Phone no')
    print('\n 4. Customer Email id')
    choice = int(input("what do you want to change? : "))
    new_data = input("Enter new value : ")
    #field=""
    if(choice==1):
        field='name'
    if(choice==2):
        field='address'
    if(choice==3):
        field='phone'
    if(choice==4):
        field='email'
    sql ='update customers set '+ field+ '="'+new_data+'" where acno='+acno+';'
    cursor.execute(sql)
    conn.commit()
    clear()
    print('\n\n Customer Information modified')
    wait=input('\n\n\n Press any key to continue...')

def close_account():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    acno=int(input("Enter your account no : "))
    sql="update customers set status='{}' where acno='{}'".format("close",acno)
    # t6= "update bank set Balance=Balance +'{}' where UserName='{}'".format(a11,u)
    cursor.execute(sql)
    conn.commit()
    clear()
    print("\n\n account closed finally...")
    wait=input('\n\n\n Press any key to continue...')


def transaction_menu():
    while True:
        clear()
        print('Transaction menu')
        print('\n 1. Deposit amount')
        print('\n 2. Withdraw amount')
        print('\n 3. Back to main menu')
        print('\n\n')
        choice = int(input("Enter your choice... : "))
        if(choice==1):
            deposit_amount()
        if(choice==1):
            withdraw_amount()
        if(choice==3):
            break


def Search_menu():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    while True:
        clear()
        print(' Search Menu')
        print('\n 1. Account no')
        print('\n 2. Aadhar no')
        print('\n 3. Phone no')
        print('\n 4. Email')
        print('\n 5. Names')
        print('\n 6. Back to Main Menu')
        print('\n\n')
        choice = int(input("what do you want to change? : "))
        field=""
        if(choice==1):
           field=acno
        if(choice==2):
           field=aadhar_no
        if(choice==3):
           field=phone
        if(choice==4):
           field=email
        if(choice==5):
           field=name
        if(choice==6):
           break
        msg='Enter '+field+';'
        value=input(msg)
        if field==acno:
            sql='Select * from customers where '+field+'='+value+';'
        else:
            print("\n\n account search results not found...") 
        cursor.execute(sql)
        conn.commit()
        clear()
        print("\n\n account search results...") 
        wait=input('\n\n\n Press any key to continue...')

def activate_account():
    conn=mysql.connector.connect(
        host='localhost', database='proj1', user='root', password='@ditu002'
    )
    cursor=conn.cursor()
    cursor.execute("use proj1")
    acno=input("Enter your account no : ")
    sql='update customers set status="active" where acno='+acno+';'
    cursor.execute(sql)
    conn.commit()
    clear()
    print('\n\n account activated')
    wait=input('\n\n\n Press any key to continue...')

def main_menu():
    while True:
        clear()
        print(' Main Menu')
        print('\n 1. Add Account')
        print('\n 2. Modify account')
        print('\n 3. Activate account')
        print('\n 4. Close account')
        print('\n 5. Transaction menu')
        print('\n 6. Search menu')
        print('\n 7. close application')
        print('\n\n')
        choice = int(input("what do you want to change? : "))
        field=""
        if(choice==1):
           add_account()
        if(choice==2):
           modify_account()
        if(choice==3):
           activate_account()
        if(choice==4):
           close_account()
        if(choice==5):
           transaction_menu()
        if(choice==6):
           Search_menu()
        if(choice==7):
           break

main_menu()

   
