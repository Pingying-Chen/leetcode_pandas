# 596. Classes More Than 5 Students

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').count().reset_index()
    df = df[df['student'] >= 5]
    return df[['class']]


import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').agg({'student': 'count'}).reset_index()
    df = df[df['student'] >= 5]
    return df[['class']]
