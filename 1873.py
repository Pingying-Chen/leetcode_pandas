# 1873. Calculate Special Bonus

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']
    employees.loc[(employees['employee_id'] % 2 == 0) | (employees['name'].str.startswith(('M'))), 'bonus'] = 0
    return employees[['employee_id', 'bonus']].sort_values(by = ['employee_id'])

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id']%2 == 1 and x['name'][0] != 'M' else 0, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by = ['employee_id'])
