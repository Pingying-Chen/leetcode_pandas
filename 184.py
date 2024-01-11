# 184. Department Highest Salary

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(department, left_on = 'departmentId', right_on = 'id', how = 'left').rename(columns = {'id_x': 'employeeId', 'name_x': 'Employee', 'salary': 'Salary', 'name_y': 'Department'})
    highest_salary_df = merged_df.groupby('Department').apply(lambda x: x[x['Salary'] == x['Salary'].max()])
    return highest_salary_df[['Department', 'Employee', 'Salary']]

import pandas as pd

def department_highest_salary(employee_df: pd.DataFrame, department_df: pd.DataFrame) -> pd.DataFrame:
    if employee_df.empty or department_df.empty:
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])
    
    merged_df = employee_df.merge(
        department_df,
        left_on='departmentId',
        right_on='id',
        how='left'
    ).rename(columns={'name_x': 'Employee', 'salary': 'Salary', 'name_y': 'Department'})
    highest_salary_df = merged_df.loc[merged_df.groupby('Department')['Salary'].idxmax()]
    return highest_salary_df[['Department', 'Employee', 'Salary']]
