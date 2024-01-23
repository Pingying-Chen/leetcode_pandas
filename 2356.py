# 2356. Number of Unique Subjects Taught by Each Teacher

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    # pandas.DataFrame.nunique: Count number of distinct elements in specified axis. Return Series with number of distinct elements. Can ignore NaN values.
    return df.rename({'subject_id': 'cnt'}, axis = 1)
