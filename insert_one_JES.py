import mysql.connector

db = mysql.connector.connect(
    host="rds-mysql-10minute-tutorial.cukxgf8os2nu.us-east-1.rds.amazonaws.com",
    user="admin",
    password="A7mioevLYTED",
    database="employee_data",
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jim", "Chicago")
cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))