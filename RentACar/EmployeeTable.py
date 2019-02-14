'''
Created on Mar 21, 2018

@author: Miroslav_Mirkovic
'''
import sqlite3
db = sqlite3.connect('RentACar.db')
cursor = db.cursor()
#cursor.execute('''DROP TABLE Employee''')
cursor.execute('''CREATE TABLE Employee(idEmployee INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, LastName TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL,DateFrom INTEGER NOT NULL, DateTo INTEGER NULL)''')

Name1 = 'Lazar'
LastName1 = 'Lazarevic'
UserName1 = 'LaLa'
Password1 ='12345'
DateFrom1='2018-01-01'


Name2 = 'Petar'
LastName2 = 'Petrovic'
UserName2 = 'PePe'
Password2 ='12346'
DateFrom2='2018-02-01'


Name3 = 'Marko'
LastName3 = 'Markovic'
UserName3 = 'MaMa'
Password3 ='12347'
DateFrom3='2018-03-01'


Name4 = 'Iva'
LastName4 = 'Ivic'
UserName4 = 'IvIv'
Password4 ='12348'
DateFrom4='2018-01-15'


Name5 = 'Bane'
LastName5 = 'Banic'
UserName5 = 'BaBa'
Password5 ='12349'
DateFrom5='2018-03-01'


Employee = [(Name1,LastName1, UserName1, Password1,DateFrom1),(Name2,LastName2, UserName2, Password2,DateFrom2),(Name3,LastName3, UserName3, Password3,DateFrom3),(Name4,LastName4, UserName4, Password4,DateFrom4),(Name5,LastName5, UserName5, Password5,DateFrom5)]
cursor.executemany('''INSERT INTO Employee(idEmployee,Name, LastName, UserName, Password,DateFrom) VALUES(NULL,?,?,?,?,?)''', Employee)
db.commit()