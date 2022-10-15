import sqlite3

conn=sqlite3.connect('prueba.db')
query="DELETE FROM STD WHERE name='bob';"
try:
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
except:
    print("Error into deletion of")