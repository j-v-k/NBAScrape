







import csv
import datetime

g = csv.reader



def replaceDate(dateString):
    d = datetime.datetime.strptime(dateString, '%b %d, %Y')
    returnedDate = d.strftime('%Y-%m-%d')
    return returnedDate

import csv
f = open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\PostSeasonWithMatch.csv', 'rb')
reader = csv.reader(f)
newList = []
for row in reader:
    newDateString = replaceDate(row[3])
    row[3] = newDateString
    newList += [row]
f.close()








def write_csv(newList,csvFile):
    
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in newList:
        g.writerow(record)

             
def Iter(newList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\PostGameLogNullDateFixed.csv', 'w')    
    write_csv(newList,csvFile)

Iter(newList)
