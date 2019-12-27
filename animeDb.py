import sqlite3

#https://likegeeks.com/python-sqlite3-tutorial/

nameOfDatabase = "animeTracker.sqlite"
db = sqlite3.connect(nameOfDatabase)
db.execute("CREATE TABLE IF NOT EXISTS anime(id INTEGER PRIMARY KEY AUTOINCREMENT, eng_title TEXT,jap_title TEXT, inserted_date TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS season(anime_id INTEGER PRIMARY KEY,number INTEGER PRIMARY KEY,name TEXT, totalEpsiodes Integer, inserted_date TEXT,
                                               FOREIGN KEY(anime_id)REFERENCES anime(id) )")
db.execute("CREATE TABLE IF NOT EXISTS epsiodes(anime_id INTEGER PRIMARY KEY,season_number INTEGER PRIMARY KEY,number INTEGER PRIMARY KEY,name TEXT,airDate TEXT, inserted_date TEXT,
                                               FOREIGN KEY(anime_id)REFERENCES season(anime_id),
                                               FOREIGN KEY(season_number)REFERENCES season(number)")


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
           
def insertNewSeason(anime_id, season_number, name ,inserted_Date):
    #Since id is a primarykey then it should be autogerneated 
    con =create_connection(nameOfDatabase).cursor()
    values= (anime_id, season_number, name ,inserted_Date)
    con.execute('INSERT INTO season(anime_id, number ,name,inserted_date) VALUES(?,?,?r,?)', values)
    con.commit()
           
def inserNewEpisode(anime_id, season_number, episode_number name , airDate, inserted_Date):
    #Since id is a primarykey then it should be autogerneated 
    con =create_connection(nameOfDatabase).cursor()
    values=(anime_id, season_number, episode_number name , airDate, inserted_Date)
    con.execute('INSERT INTO season(anime_id, season_number ,number,name,airdate,inserted_date) VALUES(?,?,?,?,?,?,?)', values)
    con.commit()


           
           
           
           
          
