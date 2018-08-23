import pymysql

host = "localhost"
user = "root"
password = ""
db = "test"
db = pymysql.connect(host, user, password, db)


cursor = db.cursor()

cursor.execute("SELECT * FROM users")

numrows = cursor.rowcount

x = 0

for x in range(x, numrows):
    row = cursor.fetchone()
    print row[0], " --- ", row[1]

db.close()