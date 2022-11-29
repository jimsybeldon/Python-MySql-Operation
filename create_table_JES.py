import mysql.connector

db = mysql.connector.connect(
    host="rds-mysql-10minute-tutorial.cukxgf8os2nu.us-east-1.rds.amazonaws.com",
    user="admin",
    password="A7mioevLYTED",
    database="employee_data",
)


cursor = db.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Table Created Successful !!!")