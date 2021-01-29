import sqlite3

conexion = sqlite3.connect("BaseDato.db")

#conexion.close()

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE USUARIOS(ID_PELI VARCHAR(50), NOMBRE_PELI VARCHAR(50), DIRECTOR VARCHAR(50), COMPANIA VARCHAR(50), GENERO VARCHAR(30), ANIO VARCHAR(30), VISTA VARCHAR(2), CALIFICACION INTEGER(5))")
#cursor.execute("INSERT INTO USUARIOS VALUES('1','Sonic','James Gun','Sega','aventura','2020','si',5)")

#cursor.execute("SELECT * FROM USUARIOS")
#usuario = cursor.fetchone()
#print(usuario)

'''
usuarios = [
    ('2','Kimetsu no yaiba','Desconocido','Imax','anime','2020','si',5),
    ('3','pokemon','satoshi taijiri','nintendo','aventura','2020','si',4),
    ('4','lego batman','Desconocido','LEGO','aventura','2016','si',3)
]

cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?,?,?,?,?,?)",usuarios)
'''
cursor.execute("SELECT * FROM USUARIOS")
usuarios = cursor.fetchall()
for i in usuarios:
    print(i)

conexion.commit()
conexion.close()

