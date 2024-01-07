# 1068. Product Sales Analysis I

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on = 'product_id', how = 'left').groupby('sale_id').agg({'product_name': 'first', 'year': 'first', 'price': 'sum'})
    return df
