import pandas as pd

def load_products():

    return pd.read_json(
        "data/raw/products/products.json"
    )

def load_holidays():

    return pd.read_json(
        "data/raw/holidays/holidays.json"
    )

def load_weather():

    return pd.read_json(
        "data/raw/weather/weather.json"
    )

def clean_products(df):

    df = df.copy()

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    def make_hashable(x):
        if isinstance(x, list):
            return tuple(make_hashable(i) for i in x)   # recurse into list
        elif isinstance(x, dict):
            return tuple(sorted((k, make_hashable(v)) for k, v in x.items()))  # recurse into dict
        elif isinstance(x, set):
            return frozenset(make_hashable(i) for i in x)  # recurse into set
        elif isinstance(x, bytearray):
            return bytes(x)
        else:
            return x

    # Apply across the whole DataFrame
    df = df.apply(lambda col: col.map(make_hashable))

    df.drop_duplicates(inplace=True)

    return df


def handle_missing_values(df):

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns

    df[numeric_cols] = (
        df[numeric_cols]
        .fillna(
            df[numeric_cols].median()
        )
    )

    return df

def remove_price_outliers(df):

    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return df[
        (df["price"] >= lower)
        &
        (df["price"] <= upper)
    ]

