
"""
Created on Mon Jun 20 15:49:20 2016

@author: James
"""

import requests


'''url = 'http://stats.nba.com/stats/boxscoretraditionalv2'+\
'?EndPeriod=10&EndRange=28800&GameID=0021500893&RangeType=0'+\
'&Season=2015-16&SeasonType=Regular+Season&StartPeriod=1'+\
'&StartRange=0'
'''
#url = 'http://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision='



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
    for i in range(int(tup2[2]),int(tup2[3])+1):
        
        last2 = int(str(i+1)[2:])
        year = str(i) + "-"+ "{0:0=2d}".format(last2)
        
        
        url = 'http://stats.nba.com/stats/playergamelog?LeagueID=00&PlayerID=' + str(tup2[0]) + '&Season=' + year + '&SeasonType=Regular+Season'
    
    
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'}
        try:
            
            response = requests.get(url, headers=headers)
            Season = response.json()['resultSets'][0]['rowSet']
            Log += [Season]
            
            
        except:
            
            print 'error'
            print i
            return
            pass
    return Log



def write_csv(info,csvFile):
    import csv
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in info:
        for row in record:
            g.writerow(row)
                
def Iter(playerTupleList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\NBAScrapeLargeFiles\\nba.csv', 'w')    
    for i in playerTupleList:
        print i[1]
        info = Get_Player_Info(i,)
        
        write_csv(info,csvFile)

Iter(playerTupleList)