DROP TABLE IF EXISTS `Gamelogs`;

CREATE TABLE  `Gamelogs`(
		
        SEASON_ID	int,
        Player_ID	int,
		Game_ID		int,
		GAME_DATE	DATE,
		MATCHUP		varchar(255),
		WL			varchar(255),
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
		PLUS_MINUS	int,
		VIDEO_AVAILABLE int,
        PlayerTeam	varchar(255),
        OppTeam		varchar(255),
        HomeAway	int,
        PostReg		varchar(255),
        IDKey int not null AUTO_INCREMENT,
        primary key (IDKey),
        FOREIGN KEY (Player_ID) REFERENCES Players(Player_ID)
        );
        
        
        
load data local infile 'C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\PostGameLogNullDateFixed.csv' 
into table seasonstats fields terminated by ','
enclosed by '"'
lines terminated by '\n';


load data local infile 'C:\\Users\\James\\Documents\\GitHub\\NBAScrapeLargeFiles\\NullFixed.csv' 
into table seasonstats fields terminated by ','
enclosed by '"'
lines terminated by '\n';
        
UPDATE gamelogs
SET PostReg='Reg'
WHERE PostReg is null;

UPDATE gamelogs
SET PostReg='Post'
WHERE PostReg is not null;

