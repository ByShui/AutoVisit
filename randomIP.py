import sqlite3
import random
import urllib.request
import re
import time
import randomUserAgent

def main():
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IPTable")
    cursor.execute("CREATE TABLE IF NOT EXISTS IPTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, ip VARCHAR(12))")
    for i in range(10):
        page = random.randint(0, 2000)
        url = (r'https://www.kuaidaili.com/free/intr/%s/' % str(page + 1))
        print(url)
        updateIP(url)
        time.sleep(2)
    # randomIP()

# 更新IPTable
def updateIP(url):
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    urllib.request.Request(url).add_header('User-Agent', randomUserAgent.randomUserAgent())
    html = urllib.request.urlopen(url).read().decode('utf-8')
    ipList = re.findall(r'\d+\.\d+\.\d+\.\d+', html)
    for ip in ipList:
        print(ip)
        cursor.execute("insert into IPTable (ip) values ('%s')" % (ip))
    print(cursor.lastrowid)
    connection.commit()
    connection.close()

# 从IPTable中随机取一个ip
def randomIP():
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS IPTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, ip VARCHAR(12))")
    lastIDCursor = cursor.execute("select * from IPTable order by _id desc limit 1")
    ipRandomID = 0
    for lastID in lastIDCursor:
        ipRandomID = random.randint(1, lastID[0])
    ipRow = cursor.execute("select * from IPTable where _id=%d" % ipRandomID)
    for ip in ipRow:
        ipStr = ip[1]
        connection.close()
        return ipStr

if __name__ == '__main__':
    main()