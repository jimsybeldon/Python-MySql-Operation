import mysql.connector

db = mysql.connector.connect(
    host="rds-mysql-10minute-tutorial.cukxgf8os2nu.us-east-1.rds.amazonaws.com",
    user="admin",
    password="A7mioevLYTED",
    database="employee_data",
)

cursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (3, )
cursor.execute(sql, val)

db.commit()

print("{} data deleted".format(cursor.rowcount))