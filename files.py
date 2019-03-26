
import sqlite3

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name STRING)")
    conn.commit()
conn.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(col_name) VALUES (?)", [file])
    conn.commit()
conn.close()

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_name FROM tbl_files")
    varFiles = cur.fetchall()
    msg = ("Files: {}".format(varFiles))
    print(msg)
