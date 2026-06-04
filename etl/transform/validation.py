import pandas as pd

def validate_products(df):

    if df.empty:
        raise ValueError("Product dataframe is empty")

    if "price" not in df.columns:
        raise ValueError("Price column missing")

    return True