import sqlite3

conn = sqlite3.connect('prueba.db')
query="""INSERT into STD(name,age,dept)values('bob',20,'cs');"""
try:
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("El registro es insertado dentro de la base de datos")
except:
    print("Error en la base de datos al insertar registro")
    conn.rollback()
conn.close()