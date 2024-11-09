import pandas as pd

def get_age(dob):
    player_dob = pd.to_datetime(dob).date()
    world_cup_start_date = pd.to_datetime("2022-11-20").date()
    age = world_cup_start_date.year - player_dob.year
    if (world_cup_start_date.month, world_cup_start_date.day) < (player_dob.month, player_dob.day):
        age -= 1
    
    return age

def get_pos(pos):
    positions = {
        'GK': 'Goalkeepr',
        'DF': 'Defender',
        'MF': 'Midfielder',
        'FW': 'Forward'
    }

    return positions[pos]