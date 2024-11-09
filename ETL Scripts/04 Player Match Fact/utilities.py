import pandas as pd
import sys,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import destination_engine
team_dim = pd.read_sql("SELECT team_key, team_name FROM Dim_team", destination_engine)
match_dim = pd.read_sql("SELECT match_key, first_team_name, second_team_name from Dim_match", destination_engine)
def get_team_key(team):
    team_key = team_dim.loc[team_dim['team_name'] == team , 'team_key']
    return team_key.values[0]

def get_opponent_team_key(team, first_team_name, second_team_name):
    opponent_team = first_team_name if first_team_name != team else second_team_name
    return get_team_key(opponent_team)

def get_match_key(first_team_name, second_team_name):
    match = match_dim[(match_dim['first_team_name'] == first_team_name) & (match_dim['second_team_name'] == second_team_name)]
    return match['match_key'].values[0]