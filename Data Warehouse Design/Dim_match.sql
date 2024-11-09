DROP TABLE IF EXISTS Dim_match;
CREATE TABLE Dim_match(
	match_key INT IDENTITY(1,1) PRIMARY KEY,
	first_team_name VARCHAR(50),
	second_team_name VARCHAR(50),
	first_team_score INT,
	second_team_score INT,
	winner VARCHAR(50),
	match_date DATE,
	stadium VARCHAR(50),
	referee NVARCHAR(50),
	round VARCHAR(25),
	penalties varchar(20),
)