'''
Created on Apr 1, 2018

@author: Miroslav_Mirkovic
'''
import sqlite3
    
def RentACar(idMember,DateFrom,idCar,idEmployee):
    var=RentACarCheck(idMember)
    if var!=-1:
        sqlite_file = 'RentACar.db'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        MemberRentACar=[(idMember,DateFrom,idCar,idEmployee)]
        c.executemany( '''INSERT INTO MemberRentACar(idMemberCar,idMember,DateFrom,DateTo,idCar,idEmployee) VALUES(NULL,?,?,NULL,?,?)''', MemberRentACar)
        conn.commit()
        rows = c.fetchall()
        for row in rows:
            print row
    else:
        print "Clan vec ima rentirano vozilo"    

def ReturnACar(idMember,DateTo):
    var=RentACarCheck(idMember)
    if var==-1:
        sqlite_file = 'RentACar.db'
        table_name = 'MemberRentACar'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('UPDATE {} SET DateTo=:DateTo where idMember=:idMember'.format(table_name),{"DateTo": DateTo, "idMember": idMember})
        conn.commit()
        row = c.fetchall()
    else:
        print "Clan nema rentirano vozilo"
        
def RentACarCheck(idMember):
    sqlite_file = 'RentACar.db'
    table_name = 'MemberRentACar'       
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT * FROM {} where idMember=? and DateTo is null'.format(table_name),[idMember])
    conn.commit()
    row = c.fetchall()
    for var in row:
        if var==row[0]:
            return -1
    return 1






