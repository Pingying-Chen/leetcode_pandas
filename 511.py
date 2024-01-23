# 511. Game Play Analysis I

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby(['player_id']).agg(player_id = ('player_id', 'first'), first_login = ('event_date', 'min'))


import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby(['player_id']).agg({'player_id': 'first', 'event_date': 'min'}).rename(columns = {'event_date': 'first_login'})


import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby(['player_id']).agg({'player_id': 'first', 'event_date': 'min'}).rename({'event_date': 'first_login'}, axis = 1)
