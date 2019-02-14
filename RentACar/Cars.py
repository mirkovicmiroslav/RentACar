'''
Created on Apr 1, 2018

@author: Miroslav_Mirkovic
'''
import sqlite3
import pandas
    
def ReadCars():
    sqlite_file = 'RentACar.db'
    table_name = 'Cars'    
    conn = sqlite3.connect(sqlite_file)
    cursor= pandas.read_sql("SELECT * FROM Cars ORDER BY Brand", conn)
    print cursor      
#    c = conn.cursor()    
#    c.execute('SELECT * FROM {}'.format(table_name))
#    rows = c.fetchall()
#    for row in rows:
#        print row



def CarsCheck(Brand):
    sqlite_file = 'RentACar.db'
    table_name = 'Cars'      
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT Brand FROM {} where Brand=?'.format(table_name),[Brand])
    row = c.fetchall()
    for var in row:
        if var==row[0]:
            return True
    return False

def CarsModelCheck(Brand, Model):
    sqlite_file = 'RentACar.db'
    table_name = 'Cars'      
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('SELECT Model FROM {} where Brand=:Brand and Model=:Model'.format(table_name),{"Brand": Brand, "Model": Model})    
    row=c.fetchall()
    for var in row:
        if var==row[0]:
            return True
    return False

def ReadCarsDetails(Brand, Model):
    sqlite_file = 'RentACar.db'
    table_name = 'Cars'    
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()    
    c.execute('SELECT * FROM {} where Brand=:Brand and Model=:Model'.format(table_name),{"Brand": Brand, "Model": Model})
    rows = c.fetchall()
    for row in rows:
        print row

def ReadCarId(Brand, Model):
    sqlite_file = 'RentACar.db'
    table_name = 'Cars'
    conn = sqlite3.connect(sqlite_file)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT idCar FROM {} where Brand=:Brand and Model=:Model'.format(table_name),{"Brand": Brand, "Model": Model})
    r=c.fetchall()[0]
    return r['idCar']