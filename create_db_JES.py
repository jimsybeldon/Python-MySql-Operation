import mysql.connector

db = mysql.connector.connect(
    host="rds-mysql-10minute-tutorial.cukxgf8os2nu.us-east-1.rds.amazonaws.com",
    user="admin",
    password="A7mioevLYTED"
)


cursor = db.cursor()
cursor.execute("CREATE DATABASE employee_data")

print("Database Created Successful !!!")