
import sqlite3

conn = sqlite3.connect('test.db')
#conn holds our connection to the database

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fname TEXT, \
    col_lname TEXT, \
    col_email TEXT \
    )")
    #so far we have established cur as shorthand for the cnnctn
    #and are creating a database
    #8:51
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES(?,?,?)", ('Sarah','Smithers','example@example.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES(?,?,?)", ('Salley','May','example@example.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
    VALUES(?,?,?)", ('K','Bacon','example@example.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE \
    col_fname = 'Sarah'")
    #store info in var to not lose
    varPerson = cur.fetchall()
    #grab all info from tuple
    #iterate all teh data out in pieces
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {} \nEmail: {}".format(item[0], item[1], item[2])
    print(msg)        
        
