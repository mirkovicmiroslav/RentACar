'''
Created on Mar 25, 2018

@author: Miroslav_Mirkovic
'''

import sqlite3
db = sqlite3.connect('RentACar.db')
cursor = db.cursor()
#cursor.execute('''DROP TABLE Employee''')
cursor.execute('''CREATE TABLE Cars(idCar INTEGER PRIMARY KEY AUTOINCREMENT, Brand TEXT NOT NULL, Model TEXT NOT NULL, Status TEXT NOT NULL, RegistrationNumber TEXT NOT NULL,DateFrom INTEGER NOT NULL, DateTo INTEGER NULL)''')

Brand1 = 'Audi'
Model1 = 'A6'
Status1 = 'Available'
RegistrationNumber1 ='11111'
DateFrom1='2018-01-01'
DateTo1='2025-01-01'

Brand2 = 'Volkswagen'
Model2 = 'Passat'
Status2 = 'Available'
RegistrationNumber2 ='22222'
DateFrom2='2018-02-01'
DateTo2='2025-01-01'


Brand3 = 'Volkswagen'
Model3 = 'Tiguan'
Status3 = 'Available'
RegistrationNumber3 ='33333'
DateFrom3='2018-03-01'
DateTo3='2025-01-01'

Brand4 = 'Mazda'
Model4 = 'CX-9'
Status4 = 'Available'
RegistrationNumber4 ='44444'
DateFrom4='2017-01-01'
DateTo4='2019-01-01'


Brand5 = 'Toyota'
Model5 = 'Prius'
Status5 = 'Available'
RegistrationNumber5 ='55555'
DateFrom5='2018-01-01'
DateTo5='2025-01-01'

Brand6='Nissan'
Model6='Frontier'
Status6 = 'Available'
RegistrationNumber6 ='66666'
DateFrom6='2018-03-01'
DateTo6='2025-01-01'

Brand7='Ford'
Model7='Focus'
Status7 = 'Available'
RegistrationNumber7 ='77777'
DateFrom7='2018-02-01'
DateTo7='2025-01-01'

Brand8='Ford'
Model8='Mustang'
Status8 = 'Available'
RegistrationNumber8 ='88888'
DateFrom8='2017-01-01'
DateTo8='2019-01-01'

Brand9='BMW'
Model9='X6'
Status9 = 'Available'
RegistrationNumber9 ='99999'
DateFrom9='2018-03-01'
DateTo9='2025-01-01'

Brand10='MercedesBenz'
Model10='SClass'
Status10 = 'Available'
RegistrationNumber10 ='15151'
DateFrom10='2018-02-15'
DateTo10='2025-01-01'

Cars = [(Brand1,Model1, Status1, RegistrationNumber1,DateFrom1,DateTo1),
            (Brand2,Model2, Status2, RegistrationNumber2,DateFrom2,DateTo2),
            (Brand3,Model3, Status3, RegistrationNumber3,DateFrom3,DateTo3),
            (Brand4,Model4, Status4, RegistrationNumber4,DateFrom4,DateTo4),
            (Brand5,Model5, Status5, RegistrationNumber5,DateFrom5,DateTo5),
            (Brand6,Model6, Status6, RegistrationNumber6,DateFrom6,DateTo6),
            (Brand7,Model7, Status7, RegistrationNumber7,DateFrom7,DateTo7),
            (Brand8,Model8, Status8, RegistrationNumber8,DateFrom8,DateTo8),
            (Brand9,Model9, Status9, RegistrationNumber9,DateFrom9,DateTo9),
            (Brand10,Model10, Status10, RegistrationNumber10,DateFrom10,DateTo10)]
cursor.executemany('''INSERT INTO Cars(idCar,Brand, Model, Status, RegistrationNumber,DateFrom,DateTo) VALUES(NULL,?,?,?,?,?,?)''', Cars)
db.commit()
