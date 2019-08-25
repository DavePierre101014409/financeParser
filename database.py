import sqlite3



nameOfDatabase = "scotiaBank.sqlite"
db = sqlite3.connect(nameOfDatabase)
db.execute("CREATE TABLE IF NOT EXISTS monthlyTransCation (name TEXT, price INTEGER, date TEXT)")
db.execute("INSERT INTO monthlyTransCation(name,price, date) VALUES('Walmart',12.99,'2018-08-01')")

#
cursor = db.cursor()
cursor.execute("SELECT * FROM monthlyTransCation")

for name ,price , date in cursor:
    print(name)
    print(price)
    print(date)

    print("-"*20)

cursor.close()
cursor.connection.commit()

db.close()

def create_connection(db_name):
    try:
        con = sqlite3.connect(db_name)
        return con

    execept Error as e:
        print(e)

    return None

def writeTranscation():
    create_connection(nameOfDatabase)

    sqlCommand= "INSERT INTO monthlyTransCation(name,price, date) VALUES('Walmart',12.99,'2018-08-01')"
