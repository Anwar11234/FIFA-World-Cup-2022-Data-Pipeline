import pandas as pd
import sys,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import source_engine, destination_engine
from get_matches_query import query
from utilities import map_pens, map_rounds

# extract
matches_df = pd.read_sql(query, source_engine)

# transform
matches_df['referee'] = matches_df['referee'].str.lower()
matches_df['stadium'] = matches_df['stadium'].str.lower()

matches_df['penalties'] = matches_df['penalties'].apply(map_pens)
matches_df['round'] = matches_df['round'].apply(map_rounds)

# load
matches_df.to_sql(
    'Dim_match', 
    destination_engine, 
    if_exists = 'append', 
    index = False
)