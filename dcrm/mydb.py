import mysql.connector

dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harathi@123",
    
)

mycursor = dataBase.cursor()

mycursor.execute("CREATE DATABASE dcrm_db")

print("Database created successfully")
