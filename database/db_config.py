# Description: This file is responsible for the database connection configuration.
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to the database
connection = mysql.connector.connect(
    user= os.getenv("USER"),
    password= os.getenv("PASSWORD"),
    host= os.getenv("HOST"),
    database= os.getenv("DATABASE"),
)

database_url = "mysql+mysqlconnector://root:1703Lunna%40@127.0.0.1/LojaRoupas"
