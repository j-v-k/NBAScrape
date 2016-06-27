







import csv
import datetime

g = csv.reader


def seperate_teams(string):
    playerTeam = string[:3]
    oppTeam = string[-3:]
    if "vs." in string:
        homeAway =1
    else:
        homeAway = 0
    return [playerTeam,oppTeam,homeAway]     


import csv
f = open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\postSeasonNullFixed.csv', 'rb')
reader = csv.reader(f)
newList = []
for row in reader:
    row += seperate_teams(row[4])
         
    newList += [row]
f.close()








def write_csv(newList,csvFile):
    
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in newList:
        g.writerow(record)

             
def Iter(newList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\postSeasonWithMatch.csv', 'w')    
    write_csv(newList,csvFile)

Iter(newList)
