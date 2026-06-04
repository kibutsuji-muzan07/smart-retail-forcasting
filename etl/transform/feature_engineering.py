import pandas as pd

def create_price_bucket(df):

    labels = [
        "cheap",
        "medium",
        "premium",
        "luxury"
    ]

    df["price_bucket"] =  pd.qcut(df["price"],
                                   q=4, 
                                   labels=labels)

    return df

def create_inventory_value(df):

    df["inventory_value"] = (
        df["price"] * df["stock"]
    )

    return df

def process_holidays(df):
    response_cell = df.loc[df["response"].notna(), "response"].iloc[0]
    df = pd.DataFrame(response_cell)

    df["date"] = pd.to_datetime(
        df["date"].apply(
            lambda x: x['iso'] if pd.notna(x) else None), 
            format='ISO8601', utc=True)

    df["month"] = (
        df["date"].dt.month_name()
    )

    df["day"] = (
        df["date"].dt.day_name()
    )

    return df


def process_weather(df):

    meta_cell = df.loc[df["data"].notna(), "data"].iloc[0]
    df = pd.DataFrame(meta_cell)

    df["is_hot"] = (
        df["temp"] > 30
    )

    df["is_humid"] = (
        df["rh"] > 70
    )

    return df