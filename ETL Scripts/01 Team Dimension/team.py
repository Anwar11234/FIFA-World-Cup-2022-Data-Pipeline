import pandas as pd
import sys, os
from get_team_ranks import ranks_df

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import source_engine, destination_engine

teams_df = pd.read_sql("SELECT  name as team_name, mgr_name as manager_name FROM team" , source_engine)

continents_df = pd.read_csv('data/continents.csv')

teams_df = pd.merge(teams_df,continents_df, on='team_name', how='inner')
teams_df = pd.merge(teams_df,  ranks_df,  on = 'team_name', how = 'inner').rename(columns= {'rank': 'world_cup_rank'})

teams_df.to_sql('Dim_team', destination_engine, if_exists = 'append', index = False)