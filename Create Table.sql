DROP TABLE IF EXISTS `Gamelogs`;

CREATE TABLE  `Gamelogs`(
		
        SEASON_ID	int,
        Player_ID	int,
		Game_ID		int,
		GAME_DATE	DATETIME,
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
        IDKey int not null AUTO_INCREMENT,
        primary key (IDKey)
        )