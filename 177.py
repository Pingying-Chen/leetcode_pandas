# 177. Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    name = 'getNthHighestSalary(' + str(N) + ')'
    unique_salaries = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset=['salary'])
    if N > 0 and N <= len(unique_salaries):
        return unique_salaries.iloc[N-1:N].rename(columns={'salary': name}).iloc[:, 1:2]
    else:
        return pd.DataFrame({name: [pd.NA]})
