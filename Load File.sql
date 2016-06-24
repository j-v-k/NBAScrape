load data local infile 'C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\nba.csv' 
into table gamelogs fields terminated by ','
  enclosed by '"'
  lines terminated by '\n'