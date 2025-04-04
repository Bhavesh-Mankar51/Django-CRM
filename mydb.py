import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.getenv('DB_PASSWORD')
)

#prepare a cursor object


cursorOject = dataBase.cursor()

cursorOject.execute("CREATE DATABASE bmco")

print("All Done!")