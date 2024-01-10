# 176. Second Highest Salary

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset=['salary']).rename(columns = {'salary': 'SecondHighestSalary'})
    if len(unique_salaries) >= 2:
        return unique_salaries.iloc[1:2, 1:2]
    else:
        return pd.DataFrame({'SecondHighestSalary': [pd.NA]})
