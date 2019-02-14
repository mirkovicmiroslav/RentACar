'''
Created on Mar 25, 2018

@author: Miroslav_Mirkovic
'''
import sqlite3
import pandas
pandas.set_option('expand_frame_repr', False)

def ReadMembers():
    sqlite_file = 'RentACar.db'
    table_name = 'Members'    
    conn = sqlite3.connect(sqlite_file)
    cursor= pandas.read_sql("SELECT * FROM {}".format(table_name), conn)        
#    c = conn.cursor()    
#    c.execute('SELECT * FROM {}'.format(table_name))
#    conn.commit()
#    rows = c.fetchall()
#    for row in rows:
#        print row
    print cursor


def ReadOneMember(idMember):
    sqlite_file = 'RentACar.db'
    table_name = 'Members'    
    conn = sqlite3.connect(sqlite_file)
#    cursor= pandas.read_sql("SELECT * FROM {} where idMember= ?".format(table_name), conn, params={'idMember': idMember})
#    print cursor       
    c = conn.cursor()    
    c.execute('SELECT * FROM {} where idMember=?'.format(table_name),[idMember])
    rows = c.fetchall()
    for row in rows:
        print row

def MembersCheck(idMember):
    sqlite_file = 'RentACar.db'
    table_name = 'Members'       
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT * FROM {} where idMember=?'.format(table_name),[idMember])
    conn.commit()
    row = c.fetchall()
    for var in row:
        if var==row[0]:
            return var
    print "Ne postoji clan sa zadatim ID-om\n"    
    return -1

def DeleteMember(idMember):
    var=MembersCheck(idMember)
    if var!=-1:
        sqlite_file = 'RentACar.db'
        table_name = 'Members'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('DELETE FROM {} where idMember=?'.format(table_name),[idMember])
        conn.commit()
        row = c.fetchall()
        sqlite_file1 = 'RentACar.db'
        table_name1 = 'MemberRentACar'
        conn1 = sqlite3.connect(sqlite_file1)
        c1 = conn1.cursor()
        c1.execute('DELETE FROM {} where idMember=?'.format(table_name1),[idMember])
        conn1.commit()
        row1 = c1.fetchall()
    else:
        print "Ne postoji clan sa zadatim ID-om"
            
def AddMember(Name,LastName,JMBG,Address,MobilePhone,Email,MemberSince,idEmployee):
    sqlite_file = 'RentACar.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    Members=[(Name, LastName, JMBG, Address,MobilePhone,Email,MemberSince,idEmployee)]
    c.executemany( '''INSERT INTO Members(idMember,Name,LastName,JMBG, Address,MobilePhone,Email,MemberSince,idEmployee) VALUES(NULL,?,?,?,?,?,?,?,?)''', Members)
    conn.commit()
    rows = c.fetchall()
    for row in rows:
        print row

def ReadMemberId(idMember):
    sqlite_file = 'RentACar.db'
    table_name = 'Members'
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT idMember FROM {} where idMember=:idMember'.format(table_name),{"idMember": idMember})
    r=c.fetchall()[0]
    return r['idMember']
