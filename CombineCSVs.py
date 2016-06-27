# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:44:09 2016

@author: James
"""

'''import csv
with open("C:\\Users\\James\\Documents\\P00000001-ALL.csv","rb") as source:
    rdr= csv.reader( source )
    with open("C:\\Users\\James\\Documents\\newfile.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[3], r[4]) )'''
            
            
GameLog = []
Matchup = []
import csv
with open("C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\Gamelog.csv","rb") as source:
    gameLogReader= csv.reader( source )
    for i in gameLogReader:
        
        GameLog  += [i]
    
with open("C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\Matchups.csv","rb") as source:
    matchupReader= csv.reader( source )
    for i in matchupReader:
        
        Matchup += [i]
csvFile =  open('C:\\Users\\James\\Documents\\GitHub\NBAScrapeLargeFiles\\GameLogsMatch.csv', 'w') 
for num, i in enumerate(GameLog):
    newRow = i + Matchup[num]
    print i[1]
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    g.writerow( newRow )
    
    
