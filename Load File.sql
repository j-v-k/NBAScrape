load data local infile 'C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\SesonStatsNullFixed.csv' 
into table seasonstats fields terminated by ','
  enclosed by '"'
  lines terminated by '\n'
  