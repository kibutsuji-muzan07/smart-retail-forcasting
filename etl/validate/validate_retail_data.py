import pandas as pd

df = pd.read_parquet(
    "data/processed/retail_features.parquet"
)

print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNegative Prices:")
print((df["price"] < 0).sum())

print("\nNegative Stock:")
print((df["stock"] < 0).sum())