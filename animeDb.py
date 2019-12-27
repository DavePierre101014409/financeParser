import sqlite3

#https://likegeeks.com/python-sqlite3-tutorial/

nameOfDatabase = "animeTracker.sqlite"
db = sqlite3.connect(nameOfDatabase)
db.execute("CREATE TABLE IF NOT EXISTS anime(id INTEGER PRIMARY KEY, eng_title TEXT,jap_title TEXT, inserted_date TEXT)")

#
cursor = db.cursor()
cursor.execute("SELECT * FROM monthlyTransCation")

for name ,price , date in cursor:
    print(name)
    print(price)
    print(date)


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

def insertNewAnime(eng_title, jap_title, inserted_Date):
    #Since id is a primarykey then it should be autogerneated 
    con =create_connection(nameOfDatabase).cursor()
    values= (eng_title, jap_title, inserted_Date)
    con.execute('INSERT INTO anime(eng_title, jap_title ,inserted_date) VALUES(?,?,?)', values)
    con.commit()
