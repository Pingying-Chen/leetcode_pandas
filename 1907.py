# 1907. Count Salary Categories

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts['income'] < 20000])
    average = len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)])
    high = len(accounts[accounts['income'] > 50000])
    return pd.DataFrame({'category': ['High Salary', 'Low Salary', 'Average Salary'], 'accounts_count': [high, low, average]})
