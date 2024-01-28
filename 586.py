# 586. Customer Placing the Largest Number of Orders

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number').count().reset_index().sort_values(by = 'order_number', ascending = False)
    return df.iloc[0:1, 0:1]
