import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="piku@2004"
)

print(mydb)