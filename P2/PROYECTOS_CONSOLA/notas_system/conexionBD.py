import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
<<<<<<< HEAD
        port=3306,
        host='localhost',
        user='root',
        password='admin',
=======
        port=3307,
        host='localhost',
        user='root',
        password='',
>>>>>>> b089ef6c5e532afcf47601aa1b79a78263122bd4
        database='bd_notas',
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    
