import sqlite3



nameOfDatabase = "scotiaBank.sqlite"
db = sqlite3.connect(nameOfDatabase)
db.execute("CREATE TABLE IF NOT EXISTS monthlyTransCation (name TEXT, price INTEGER, date TEXT)")
db.execute("INSERT INTO monthlyTransCation(name,price, date) VALUES('Walmart',12.99,'2018-08-01')")


cursor = db.cursor()
cursor.execute("SELECT * FROM monthlyTransCation")

for name ,price , date in cursor:
    print(name)
    print(price)
    print(date)

    print("-"*20)
db.close()
