import sqlite3

conexion = sqlite3.connect("Peliculas.db")

cursor = conexion.cursor()
#
#cursor.execute('''
#        CREATE TABLE PELICULAS(
#                ID_PELI INTEGER PRIMARY KEY AUTOINCREMENT, 
#                NOMBRE_PELI VARCHAR(50), 
#                DIRECTOR VARCHAR(50), 
#                COMPANIA VARCHAR(50), 
#                GENERO VARCHAR(30),
#                ANIO VARCHAR(30), 
#                VISTA VARCHAR(2), 
#                CALIFICACION INTEGER(5))
                
#               ''')

#Ingresar
# peliculas = [
#     ('Kimetsu no yaiba','Desconocido','Imax','anime','2020','si',5),
#     ('pokemon','satoshi taijiri','nintendo','aventura','2020','si',4),
#     ('lego batman','Desconocido','LEGO','aventura','2016','si',3)
# ]

# cursor.executemany("INSERT INTO PELICULAS VALUES(NULL,?,?,?,?,?,?,?)",peliculas)
'''
#busqueda
cursor.execute("SELECT * FROM PELICULAS WHERE DIRECTOR='Desconocido'")
peliculas = cursor.fetchall()
print (peliculas)

#actualizar
cursor.execute("UPDATE PELICULAS SET DIRECTOR='Mario Dzul' WHERE DIRECTOR='Desconocido'")
'''
'''
#Eliminar
cursor.execute("DELETE FROM PELICULAS WHERE ID_PELI = 2")
'''

A = str(input("Que quieres hacer? \n1) Consultar todas las pelis 2)Filtrar peliculas 3)Agregar una nueva Peli 4)Marcar como vista 5)Eliminar pelicula \n"))

if A == "1":
    print("Son todas las peliculas disponibles hasta el momento")
    cursor.execute("SELECT * FROM PELICULAS")
    peliculas = cursor.fetchall()
    for i in peliculas:
        print (i)
        
else:
           
    if A == "2":
        B = str(input("Filtro para aplicar 1)ID 2)GENERO 3)COMPAÑIA 4)PRODUCTORA 5) CALIFICACION 6) VISTA \n "))
        if B == "1":
            B = str(input("DAME EL ID"))
            cursor.execute("SELECT * FROM PELICULAS WHERE ID_PELI='{B}'")
            peliculas = cursor.fetchall()
            print (peliculas)
    
        
conexion.commit()
conexion.close()