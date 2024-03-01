# 2738. Count Occurrences in Text

import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull = files['content'].astype(str).str.contains(r'(\s+bull\s+)', regex=True, case=False).sum()
    bear = files['content'].astype(str).str.contains(r'(\s+bear\s+)', regex=True, case=False).sum()
    data = {'word': ['bull', 'bear'], 'count': [bull, bear]}
    return pd.DataFrame(data)
