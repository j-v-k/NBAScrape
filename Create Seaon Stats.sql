DROP TABLE IF EXISTS `seasonstats`;
CREATE TABLE  SeasonStats(
		
        Player_ID	int,
		SEASON		varchar(255),
        Leauge_ID	int,
        Team_num	int,
        Team_ID   	varchar(255),
        Player_Age	int, 
        GP			int, 
        GS			int, 
		MIN			int,
		FGM			int,
		FGA			int,
		FG_PCT		DECIMAL(4,3),
		FG3M		int,
		FG3A		int,
		FG3_PCT		DECIMAL(4,3),
		FTM			int,
		FTA			int,
		FT_PCT		DECIMAL(4,3),
		OREB		int,
		DREB		int,
		REB			int,
		AST			int,
		STL			int,
		BLK			int,
		TOV			int,
		PF			int,
		PTS			int,
        PostReg		varchar(255),
        IDKey int not null AUTO_INCREMENT,
        primary key (IDKey),
        FOREIGN KEY (Player_ID) REFERENCES Players(Player_ID)
        );
        

load data local infile 'C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\SesonStatsNullFixed.csv' 
into table seasonstats fields terminated by ','
enclosed by '"'
lines terminated by '\n';



UPDATE seasonstats
SET PostReg='Reg'
WHERE PostReg like'%g%';

UPDATE seasonstats
SET PostReg='Post'
WHERE PostReg not like'%g%';

Delete from seasonstats
WHERE Team_id ='TOT';