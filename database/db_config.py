# Description: This file is responsible for the database connection configuration.
import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    user= 'root',
    password= '1703Lunna@',
    host= '127.0.0.1',
    database= 'LojadeRoupas',
)

database_url = "mysql+mysqlconnector://root:1703Lunna%40@127.0.0.1/LojaRoupas"
