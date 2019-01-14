import mysql.connector

mydb = mysql.connector.connect(
  host="xx__hostName__xx",
  user="xx__uName__xx",
  passwd="xx__passWd__xx",
  database="xx__dataBase__xx"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM xx__tableName__xx")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
