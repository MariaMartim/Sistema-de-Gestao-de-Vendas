import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    user= 'root',
    password= '1703Lunna@',
    host= '127.0.0.1',
    database= 'LojaRoupas',
)

cursor = connection.cursor()

comando = ''
cursor.execute(comando)
connection.commit() #editar o banco de dados
resultado = cursor.fetchall() #ler o banco de dados

cursor.close()
connection.close()