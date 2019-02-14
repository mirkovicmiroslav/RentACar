'''
Created on Mar 21, 2018

@author: Miroslav_Mirkovic
'''
import sqlite3

def ReadEmployee():
    sqlite_file = 'RentACar.db'
    table_name = 'Employee'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()    
    c.execute('SELECT * FROM {}'.format(table_name))
    rows = c.fetchall()
    for row in rows:
        print row

def UsernameCheck(UserName):
    sqlite_file = 'RentACar.db'
    table_name = 'Employee'  
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT UserName FROM {} where UserName=?'.format(table_name),[UserName])
    row = c.fetchall()
    for var in row:
        if var==row[0]:
            return 1
    return 0

def PasswordCheck(UserName, Password):
    sqlite_file = 'RentACar.db'
    table_name = 'Employee'  
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT Password FROM {} where Username=:UserName and Password=:Password'.format(table_name),{"UserName": UserName, "Password": Password})    
    row=c.fetchall()
    for var in row:
        if var==row[0]:
            return 1
    return 0

def myId(UserName, Password):
    sqlite_file = 'RentACar.db'
    table_name = 'Employee'
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT idEmployee FROM {} where Username=:UserName and Password=:Password'.format(table_name),{"UserName": UserName, "Password": Password})
    r=c.fetchall()[0]
    return r['idEmployee']