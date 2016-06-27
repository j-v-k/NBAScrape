







import csv
import datetime

g = csv.reader




import csv
f = open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\NBASeasonStats.csv', 'rb')
reader = csv.reader(f)
newList = []
for row in reader:
    for num,i in enumerate(row):
         if i == "":  
            
            row[num] = "\N"
         else:
            pass
    newList += [row]
f.close()








def write_csv(newList,csvFile):
    
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in newList:
        g.writerow(record)

             
def Iter(newList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\SesonStatsNullFixed.csv', 'w')    
    write_csv(newList,csvFile)

Iter(newList)
