import mysql.connector

# Conectarse a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda"
)

# Realizar una consulta
cursor = connection.cursor()
cursor.execute("SELECT * FROM factura")

# Imprimir los resultados
for row in cursor:
    print(row)

# Cerrar la conexión
connection.close()