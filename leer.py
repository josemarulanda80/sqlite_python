from select import select
import sqlite3

conn = sqlite3.connect('prueba.db')
select = "SELECT * FROM STD"
cursor= conn.cursor()
cursor.execute(select)

while True:
    record=cursor.fetchone()
    if record==None:
        break
    print(record)