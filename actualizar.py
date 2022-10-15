
import sqlite3
conn = sqlite3.connect('prueba.db')
query="UPDATE STD SET age=25 WHERE name='bob';"
try:
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Conectar ")
except:
    print("registro actualizado")