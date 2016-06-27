DROP TABLE IF EXISTS `gamelogspost`;
DROP TABLE IF EXISTS `seasonstats`;
DROP TABLE IF EXISTS `gamelogs`;
DROP TABLE IF EXISTS `Players2`;
DROP TABLE IF EXISTS `Players`;


CREATE TABLE  `Players`(
		
        
        Player_ID	int,
		firstLast	varchar(255),
		StartYear	year,
		EndYear		year,
        firstName	varchar(255),
        lastName	varchar(255),
		
        primary key (Player_ID)
        
        );


load data local infile 'C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\playersSeperatedNames.csv' 
into table seasonstats fields terminated by ','
enclosed by '"'
lines terminated by '\n';