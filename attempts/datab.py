import MySQLdb
import sys
db = MySQLdb.connect('','','','')
cursor = db.cursor()
def begin():
    print """Select Function
    1. Add
    2. Delete
    3. Inquire
    4. Modify"""
    return str(raw_input("Select the input:"))
try:
    choice = begin()
    if choice == '1':
        nam = raw_input("Enter name:")
        age = int(raw_input("Enter Age"))
        sql = "insert into table1(name,age) values('%s','%d')"%(nam,age)
        cursor.execute(sql)
        db.commit()
    if choice == '2':
        nam = raw_input("Enter name:")
        sql = "delete from table1 where name = '%s'"%(nam)
        cursor.execute(sql)
        db.commit()
    if choice == '3':
        nam = raw_input("Enter name:")
        sql = "select * from table1 where name = '%s'"%(nam)
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            print ("Name %s Age %d") %(row[0],row[1])
    if choice == '4':
        nam = raw_input("Enter name:")
        age = raw_input("Enter new age:")
        sql = "update table1 set age = '%d' where name = '%s'"%(age,nam)
        cursor.execute(sql)
        db.commit()
    db.close()
except:
    db.rollback()
    e = sys.exc_info()[0]
    print e

    
                    
