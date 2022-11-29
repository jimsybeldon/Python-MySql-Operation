import mysql.connector

db = mysql.connector.connect(
    host="rds-mysql-10minute-tutorial.cukxgf8os2nu.us-east-1.rds.amazonaws.com",
    user="admin",
    password="A7mioevLYTED"
)

if db.is_connected():
    print("Database Connected")