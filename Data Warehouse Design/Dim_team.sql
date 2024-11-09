DROP TABLE IF EXISTS Dim_team;
CREATE TABLE Dim_team(
	team_key INT IDENTITY(1,1) PRIMARY KEY,
	team_name VARCHAR(50),
	manager_name NVARCHAR(50),
	continent VARCHAR(50),
	world_cup_rank INT,
)