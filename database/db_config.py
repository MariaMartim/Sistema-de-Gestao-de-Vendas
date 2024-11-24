from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

# Connect to the database
connection = mysql.connector.connect(
    user= 'root',
    password= '1703Lunna@',
    host= '127.0.0.1',
    database= 'LojadeRoupas',
)

print(connection) # <mysql.connector.connection.MySQLConnection object at 0x7f8b3c1b3d30>