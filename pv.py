import requests
import time
import sqlite3

import randomUserAgent
import randomIP
import randomURL

def openUrl(ip, agent, url):
    try:
        headers = {'User-Agent' : agent}
        proxies = {'http' : ip}
        requests.get(url, headers=headers, proxies=proxies, verify=True)
    except requests.exceptions.ProxyError:
        print("\nrequests.exceptions.ProxyError.\nplease modify system agent.")
    else:
        print("Access to success.")

if __name__ == '__main__':
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS IPTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, ip VARCHAR(12))")
    cursor.execute("CREATE TABLE IF NOT EXISTS AgentTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, agent VARCHAR(1024))")
    cursor.execute("CREATE TABLE IF NOT EXISTS URLTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, url VARCHAR(512))")
    print("成功连接到数据库")

    for i in range(10000):
        ip = randomIP.randomIP()
        agent = randomUserAgent.randomUserAgent()
        url = randomURL.randomURL()
        print("IP: " + ip + "\n" + "User-Agent: " + agent + "\n" + "URL: " + url + "\n" + "Count: " + str(i+1))
        openUrl(ip, agent, url)
        time.sleep(1)

    connection.close()
