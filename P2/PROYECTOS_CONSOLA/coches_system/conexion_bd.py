<<<<<<< HEAD
import mysql.connector

try:
    conexion=mysql.connector.connect(
    port="3306",    
    host="127.0.0.1",
    user="root",
    password="admin",
    database="bd_coches"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la base de datos... Verifique")

=======
import mysql.connector

try:
    conexion=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="coches"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la base de datos... Verifique")

>>>>>>> b089ef6c5e532afcf47601aa1b79a78263122bd4
