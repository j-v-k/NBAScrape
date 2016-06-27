
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
    playerListList = []
    for i in players:
        List = [i[0], i[1],i[4],i[5]]
        playerListList += [List]
    return playerListList

playerListList = GetPlayers_List()





def write_csv(info,csvFile):
    import csv
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    g.writerow(info)
                
def Iter(playerListList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\NBAScrapeLargeFiles\\Players.csv', 'w')    
    for i in playerListList:
        print i[1]
        #info = Get_Player_Info(i,)
        write_csv(i,csvFile)

Iter(playerListList)