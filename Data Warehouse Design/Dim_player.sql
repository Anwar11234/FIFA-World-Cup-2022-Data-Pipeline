DROP TABLE IF EXISTS Dim_player;
CREATE TABLE Dim_player(
	player_key INT IDENTITY(1,1) PRIMARY KEY,
	team_name VARCHAR(50),
	player_name VARCHAR(50),
	position VARCHAR(10),
	age INT,
	club VARCHAR(50),
)