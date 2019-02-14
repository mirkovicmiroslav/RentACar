import sqlite3
db = sqlite3.connect('RentACar.db')
cursor = db.cursor()
#cursor.execute('''DROP TABLE Members''')
cursor.execute('''CREATE TABLE MemberRentACar(idMemberCar INTEGER PRIMARY KEY AUTOINCREMENT, idMember INTEGER NOT NULL, DateFrom INTEGER NOT NULL, DateTo INTEGER NULL, idCar INTEGER, idEmployee INTEGER, FOREIGN KEY (idMember) REFERENCES Members(idMember),FOREIGN KEY (idCar) REFERENCES Cars(idCar), FOREIGN KEY (idEmployee) REFERENCES Employee(idEmployee) )''')

idMember1 = 1
DateFrom1='2018-01-01'
DateTo1='2018-01-05'
idCar1=1
idEmployee1=5

idMember2 = 1
DateFrom2='2018-01-10'
DateTo2='2018-01-15'
idCar2=5
idEmployee2=4

idMember3 = 1
DateFrom3='2018-02-15'
DateTo3='2018-02-20'
idCar3=10
idEmployee3=3

idMember4 = 2
DateFrom4='2018-02-01'
DateTo4='2018-02-10'
idCar4=5
idEmployee4=1

idMember5 = 2
DateFrom5='2018-01-15'
DateTo5='2018-01-25'
idCar5=1
idEmployee5=5

idMember6 =3
DateFrom6='2018-02-01'
DateTo6='2018-02-06'
idCar6=1
idEmployee6=4

idMember7 =3
DateFrom7='2018-01-01'
DateTo7='2018-01-03'
idCar7=5
idEmployee7=3

idMember8 =3
DateFrom8='2018-01-05'
DateTo8='2018-01-15'
idCar8=2
idEmployee8=2

idMember9 = 4
DateFrom9='2018-03-15'
DateTo9='2018-03-25'
idCar9=3
idEmployee9=1

idMember10 = 4
DateFrom10='2018-01-01'
DateTo10='2018-01-09'
idCar10=10
idEmployee10=1

idMember11 = 5
DateFrom11='2018-03-01'
DateTo11='2018-03-11'
idCar11=1
idEmployee11=2

idMember12 = 5
DateFrom12='2018-01-20'
DateTo12='2018-01-25'
idCar12=3
idEmployee12=3

idMember13 = 6
DateFrom13='2018-02-12'
DateTo13='2018-02-18'
idCar13=2
idEmployee13=4

idMember14 = 6
DateFrom14='2018-03-01'
DateTo14='2018-03-06'
idCar14=10
idEmployee14=5

idMember15 = 7
DateFrom15='2018-03-01'
DateTo15='2018-03-07'
idCar15=5
idEmployee15=1

MemberRentACar = [(idMember1,DateFrom1,DateTo1,idCar1,idEmployee1),
            (idMember2,DateFrom2,DateTo2,idCar2,idEmployee2),
            (idMember3,DateFrom3,DateTo3,idCar3,idEmployee3),
            (idMember4,DateFrom4,DateTo4,idCar4,idEmployee4),
            (idMember5,DateFrom5,DateTo5,idCar5,idEmployee5),
            (idMember6,DateFrom6,DateTo6,idCar6,idEmployee6),
            (idMember7,DateFrom7,DateTo7,idCar7,idEmployee7),
            (idMember8,DateFrom8,DateTo8,idCar8,idEmployee8),
            (idMember9,DateFrom9,DateTo9,idCar9,idEmployee9),
            (idMember10,DateFrom10,DateTo10,idCar10,idEmployee10),
            (idMember11,DateFrom11,DateTo11,idCar11,idEmployee11),
            (idMember12,DateFrom12,DateTo12,idCar12,idEmployee12),
            (idMember13,DateFrom13,DateTo13,idCar13,idEmployee13),
            (idMember14,DateFrom14,DateTo14,idCar14,idEmployee14),
            (idMember15,DateFrom15,DateTo15,idCar15,idEmployee15)]
cursor.executemany('''INSERT INTO MemberRentACar(idMemberCar,idMember,DateFrom,DateTo,idCar,idEmployee) VALUES(NULL,?,?,?,?,?)''', MemberRentACar)
db.commit()
