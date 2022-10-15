import sqlite3
try:
    #De esta manera se conecta a una base de datos sqlite3
    conn =sqlite3.connect('prueba.db')
    #Se crea un puntero
    cursor=conn.cursor()
    #SQL para crear la tabla
    cretretable='''CREATE TABLE STD(stdid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) NOT NULL, age INTEGER,dept TEXT(20));'''
    #con execute se realiza operaciones sql
    conn.execute(cretretable)
    #Se cerro el cursor 
    print("Database Connection and creation is successfully created")

    cursor.close()
except sqlite3.Error as error:
    print(f"Message: {error}")

finally:
    if conn:
        conn.close()