







import csv
import datetime

g = csv.reader


def seperate_names(string):
    indexComma = string.find(",")
    lastName = string[:indexComma]
    firstName = string[indexComma +2:]
    
    return [firstName, lastName]     


import csv
f = open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\Players.csv', 'rb')
reader = csv.reader(f)
newList = []
for row in reader:
    row += seperate_names(row[1])
         
    newList += [row]
f.close()








def write_csv(newList,csvFile):
    
    
    g = csv.writer(csvFile, delimiter=',',lineterminator = '\n')
    for record in newList:
        g.writerow(record)

             
def Iter(newList):
    csvFile =  open('C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\playersSeperatedNames.csv', 'w')    
    write_csv(newList,csvFile)

Iter(newList)
