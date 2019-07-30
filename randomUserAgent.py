import sqlite3
import random
from selenium import webdriver

# 更新AgentTable
def updateUserAgent(url=r'http://www.useragentstring.com/pages/useragentstring.php?typ=Browser'):
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    browser = webdriver.Firefox()
    browser.get(url)
    agentLiList = browser.find_elements_by_tag_name("li")
    for agentLi in agentLiList:
        agentAList = agentLi.find_elements_by_tag_name("a")
        for agent in agentAList:
            str = agent.get_attribute("text").strip()
            print(str)
            cursor.execute("insert into AgentTable (agent) values ('%s')" % (str))
    print(cursor.lastrowid)
    connection.commit()
    browser.close()
    connection.close()

# 从AgentTable中随机取一个user-agent
def randomUserAgent():
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS AgentTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, agent VARCHAR(1024))")
    lastIDCursor = cursor.execute("select * from AgentTable order by _id desc limit 1")
    userAgentRandomID = 0
    for lastID in lastIDCursor:
        userAgentRandomID = random.randint(1, lastID[0])
    userAgentRow = cursor.execute("select * from AgentTable where _id=%d" % userAgentRandomID)
    for userAgent in userAgentRow:
        agentStr = userAgent[1]
        connection.close()
        return agentStr

if __name__ == '__main__':
    connection = sqlite3.connect("pvIPAndAgent.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE AgentTable")
    cursor.execute("CREATE TABLE IF NOT EXISTS AgentTable(_id INTEGER PRIMARY KEY AUTOINCREMENT, agent VARCHAR(1024))")
    updateUserAgent()
    # randomUserAgent()