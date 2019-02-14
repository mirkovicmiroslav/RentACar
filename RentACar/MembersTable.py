'''
Created on Apr 1, 2018

@author: Miroslav_Mirkovic
'''
import sqlite3
db = sqlite3.connect('RentACar.db')
cursor = db.cursor()
#cursor.execute('''DROP TABLE Members''')
cursor.execute('''CREATE TABLE Members(idMember INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, LastName TEXT NOT NULL, JMBG TEXT NOT NULL, Address TEXT NOT NULL, MobilePhone TEXT NOT NULL, Email TEXT NOT NULL, MemberSince INTEGER NOT NULL, idEmployee INTEGER, FOREIGN KEY (idEmployee) REFERENCES Employee(idEmployee) )''')

Name1 = 'Tatijana'
LastName1 = 'Tatic'
JMBG1 ='0101999841234'
Address1='Bulevar Oslobodjenja 47 Novi Sad'
MobilePhone1='060123456'
Email1='tatic.t@gmail.com'
MemberSince1='2018-01-01'
idEmployee1=5

Name2 = 'Ivana'
LastName2 = 'Ivanovic'
JMBG2 ='1212998841234'
Address2='Bulevar Evrope 14 Novi Sad'
MobilePhone2='060111111'
Email2='ivanovic.i@gmail.com'
MemberSince2='2018-02-01'
idEmployee2=1

Name3 = 'Radovan'
LastName3 = 'Radovanovic'
JMBG3 ='1111997859876'
Address3='Bulevar Mihajla Pupina 6 Novi Sad'
MobilePhone3='060222222'
Email3='radovanovic.r@gmail.com'
MemberSince3='2018-02-01'
idEmployee3=4

Name4 = 'Zivko'
LastName4 = 'Zivkovic'
JMBG4 ='1010996854567'
Address4='Somborski bulevar 27 Novi Sad'
MobilePhone4='060333333'
Email4='zivkovic.z@gmail.com'
MemberSince4='2018-03-15'
idEmployee4=1

Name5 = 'Djura'
LastName5 = 'Djuric'
JMBG5 ='0909995854646'
Address5='Bulevar Cara Lazara 11 Novi Sad'
MobilePhone5='060444444'
Email5='djuric.dj@gmail.com'
MemberSince5='2018-03-01'
idEmployee5=2

Name6 = 'Aleksa'
LastName6 = 'Aleksic'
JMBG6 ='0808994857777'
Address6='Bulevar Cara Dusana 98 Novi Sad'
MobilePhone6='060555555'
Email6='aleksic.a@gmail.com'
MemberSince6='2018-02-12'
idEmployee6=4

Name7 = 'Stana'
LastName7 = 'Stanic'
JMBG7 ='0707993849999'
Address7='Bulevar Despota Stefana 1 Novi Sad'
MobilePhone7='060666666'
Email7='stanic.s@gmail.com'
MemberSince7='2018-03-01'
idEmployee7=1

Members = [(Name1, LastName1, JMBG1, Address1,MobilePhone1,Email1,MemberSince1,idEmployee1),
            (Name2, LastName2, JMBG2, Address2,MobilePhone2,Email2,MemberSince2,idEmployee2),
            (Name3, LastName3, JMBG3, Address3,MobilePhone3,Email3,MemberSince3,idEmployee3),
            (Name4, LastName4, JMBG4, Address4,MobilePhone4,Email4,MemberSince4,idEmployee4),
            (Name5, LastName5, JMBG5, Address5,MobilePhone5,Email5,MemberSince5,idEmployee5),
            (Name6, LastName6, JMBG6, Address6,MobilePhone6,Email6,MemberSince6,idEmployee6),
            (Name7, LastName7, JMBG7, Address7,MobilePhone7,Email7,MemberSince7,idEmployee7)]
cursor.executemany('''INSERT INTO Members(idMember,Name,LastName,JMBG, Address,MobilePhone,Email,MemberSince,idEmployee) VALUES(NULL,?,?,?,?,?,?,?,?)''', Members)
db.commit()
