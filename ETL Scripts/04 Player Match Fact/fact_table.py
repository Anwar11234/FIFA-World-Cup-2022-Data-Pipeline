import pandas as pd
import sys,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import destination_engine
from utilities import *

player_dim = pd.read_sql("SELECT * FROM Dim_player", destination_engine)
player_match_fact = pd.read_csv('player_match_cleaned.csv')

# mismatched name between the fact table and the player dimension
player_match_fact.loc[player_match_fact['player'] == 'kevin rodriguez', 'player'] = 'kevin jauch'

player_match_fact = pd.merge(player_match_fact, player_dim, left_on='player', right_on='player_name', how = 'inner')

player_match_fact.drop(columns=[
    'player','shirtnumber','position_x', 'age_x', 'club_x','team_name', 'player_name',  
    'position_y', 'age_y', 'club_y'
], inplace=True)


player_match_fact['match_key'] = player_match_fact.apply(
    lambda row: get_match_key(row['first_team_name'], row['second_team_name']), axis=1
)

player_match_fact['team_key'] = player_match_fact.apply(
    lambda row: get_team_key(row['team']), axis=1
)

player_match_fact['opponent_team_key'] = player_match_fact.apply(
    lambda row: get_opponent_team_key(row['team'], row['first_team_name'], row['second_team_name']), axis=1
)

player_match_fact.drop(columns = [
    'team','first_team_name', 'second_team_name'
], inplace=True)

key_columns = list(player_match_fact.columns[-4:])
remaining_columns = list(player_match_fact.columns[:-4])
player_match_fact = player_match_fact[key_columns + remaining_columns]

player_match_fact = player_match_fact.rename(
    columns= {
        'minutes': 'minutes_played',
        'shots': 'total_shots',
        'cards_yellow': 'yellow_cards', 
        'cards_red': 'red_cards',
        'passes_completed':'completed_passes',
        'npxg': 'non_penality_xg',
        'sca': 'shot_creating_actions',
        'gca': 'goal_creating_actions',
        'passes': 'total_passes',
        'passes_completed': 'completed_passes',
        'passes_pct': 'completed_pass_percentage'
    }
)

player_match_fact.to_sql(
    'Player_Team_Performance_Fact',
    destination_engine,
    if_exists='append',
    index=False
)