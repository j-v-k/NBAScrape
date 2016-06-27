
"""
Created on Mon Jun 20 15:49:20 2016

@author: James
"""

import requests





def GetPlayers_List():
    url = 'http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2015-16'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'}
    response = requests.get(url, headers=headers)
    players = response.json()['resultSets'][0]['rowSet']
    playerTupleList = []
    for i in players:
        tup = (i[0], i[1],i[4],i[5])
        playerTupleList += [tup]
    return playerTupleList


playerTupleList = GetPlayers_List()



def Get_Player_Info(tup2):
        Log = []
    
        url = 'http://stats.nba.com/stats/playercareerstats?LeagueID=00&PerMode=Totals&PlayerID=' + str(tup2[0]) 
    
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'}
        try:
            
            response = requests.get(url, headers=headers)
            RegularSeason = response.json()['resultSets'][0]['rowSet']
            PostSeason = response.json()['resultSets'][2]['rowSet']
            
            
            
        except:
            
            print 'error'
            print tup2[1]
            return
        return (RegularSeason, PostSeason)



def write_csv(info,csvFile):
    import csv
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in info[0]:
        print record
        g.writerow(record + ["Reg"])
    for record in info[1]:
        g.writerow(record + ["Post"])
                
def Iter(playerTupleList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\NBAScrapeLargeFiles\\nbaSeasonStats.csv', 'w')    
    for i in playerTupleList:
        print i[1]
        info = Get_Player_Info(i,)
        
        write_csv(info,csvFile)

Iter(playerTupleList)
