# 1050. Actors and Directors Who Cooperated At Least Three Times

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).agg(count=('director_id', 'count')).reset_index()
    return df[df['count']>=3][['actor_id', 'director_id']]
