import sqlite3
import random

def randomURL():
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS URLTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, url VARCHAR(512))")
    lastIDCursor = cursor.execute("select * from URLTable order by _id desc limit 1")
    urlRandomID = 0
    for lastID in lastIDCursor:
        urlRandomID = random.randint(1, lastID[0])
    urlRow = cursor.execute("select * from URLTable where _id=%d" % urlRandomID)
    for url in urlRow:
        urlStr = url[1]
        connection.close()
        return urlStr

if __name__ == '__main__':
    randomURL()