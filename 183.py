# 183. Customers Who Never Order

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left')
    df = df[pd.isna(df['customerId'])]
    df.rename(columns = {'name': 'Customers'}, inplace = True)
    return df[['Customers']]


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers['filter'] = customers['id'].isin(orders['customerId'])
    return pd.DataFrame({'Customers':customers[customers['filter']==False]['name']})


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ans = customers[~customers["id"].isin(orders["customerId"])]["name"].values
    return pd.DataFrame(ans, columns=["Customers"])
