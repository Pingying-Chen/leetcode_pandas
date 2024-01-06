# 1667. Fix Names in a Table

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize() # Converts first character to uppercase and remaining to lowercase
    return users.sort_values(by = 'user_id')
