import mysql.connector

try:
    conexion=mysql.connector.connect(
        port="3307",
        host='localhost',
        user='root',
        password='',
        database='bd_estudiante'
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la BD verifique ...")    

