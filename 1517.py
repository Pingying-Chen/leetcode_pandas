# 1517. Find Users With Valid E-Mails

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][-.\w]*@leetcode\.com$'
    return users[users['mail'].str.match(pattern)]
