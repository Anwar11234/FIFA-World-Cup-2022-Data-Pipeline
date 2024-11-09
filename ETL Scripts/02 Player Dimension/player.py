import pandas as pd
import sys,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import source_engine, destination_engine
from utilities import get_age, get_pos

# Extract
players_df = pd.read_csv('data/players.csv')

# # Transform
players_df['age'] = players_df.birth_date.apply(get_age)

players_df['position'] = players_df.position.apply(get_pos)

players_df.drop(columns= ['shirtnumber', 'birth_date', 'birth_place', 'games', 'goals', 'minutes'], inplace=True, axis = 1)

players_df.rename(columns = {'team': 'team_name', 'player': 'player_name'}, inplace=True)

# load
players_df.to_sql(
    'Dim_player', 
    destination_engine, 
    if_exists = 'append', 
    index = False
)