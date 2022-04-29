import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "API_MYSQL"
)

myCursor = mydb.cursor()

sql = "INSERT INTO karyawan (nama, pekerjaan, usia) VALUES (%s.%s,%s)"
sql = "INSERT INTO karyawan (nama, pekerjaan, usia) VALUES (%s,%s,%s)"

val = ("Okta Ari", "Programmer", 20)
myCursor.execute(sql,val)
mydb.commit()
myCursor.close()