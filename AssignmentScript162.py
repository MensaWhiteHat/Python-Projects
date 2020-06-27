import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_extention(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_hasTxt \
    )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('information.docx',))
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('Hello.txt',))
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('myImage.png',))
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('Movie.mpg',))
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('World.txt',))
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('data.pdf',))
    cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
    VALUES (?)", ('myPhoto.jpg',))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
fileList = ('information.docx','Hello.txt','myImage.png','Movie.mpg','World.txt','data.pdf','myPhoto.jpg')
with conn:
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_extention(col_hasTxt)\
            VALUES (?)", (file,))
        print(file)
        #print(os.path.join(dirloc, file))

        
