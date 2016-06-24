
"""
Created on Mon Jun 20 15:49:20 2016

@author: James
"""

import requests

import MySQLdb
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="tintin",  # your password
                     db="nba")


def AddPlayer():
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    cursor = db.cursor()
    cursor.execute("select Matchup from gamelogs" )
    data = cursor.fetchall()
    return data
y=AddPlayer()

def newList(y):
    newList = []
    for i in y:
        LargeTup = i[0]
        playerTeam = LargeTup[:3]
        Opponent = LargeTup[-3:]
        if "vs" in LargeTup[4:8]:
            homeAway = 1
        else:
            homeAway = 0
        newList += [[playerTeam,Opponent,homeAway]]
    return newList



def write_csv(newList,csvFile):
    import csv
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in newList:
        g.writerow(record)

newList = newList(y)               
def Iter(newList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\\NBAScrape\\Matchups.csv', 'w')    
    write_csv(newList,csvFile)


Iter(newList)


