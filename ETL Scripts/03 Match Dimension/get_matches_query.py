query = """
    select 
    m.Date as match_date, 
    m.T1_name as first_team_name, 
    m.T2_name as second_team_name, 
    m.T1_score as first_team_score, 
    m.T2_score as second_team_score, 
    case when round is null then 32 else round end as round, 
    case when T1_score > T2_score then m.T1_name 
        when T1_score < T2_score then m.T2_name
        else 'Draw' end as winner,
    Pens as penalties, 
    stadium, 
    referee
    from Match m
    left join group_matches gm
    on m.T1_name = gm.T1_name and m.T2_name = gm.T2_name
    left join knockout_matches km
    on m.T1_name = km.T1_name and m.T2_name = km.T2_name
"""