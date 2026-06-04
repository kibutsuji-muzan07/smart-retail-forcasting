import os, sys
sys.path.insert(0, os.getcwd())
import pandas as pd
import json

from etl.transform.clean_data import *
from etl.transform.validation import *
from etl.transform.feature_engineering import *
from etl.transform.merge_datasets import *

products = load_products()

holidays = load_holidays()

weather = load_weather()

validate_products(products)

products = clean_products(products)

products = handle_missing_values(
    products
)

products = remove_price_outliers(
    products
)

products = create_price_bucket(
    products
)

products = create_inventory_value(
    products
)

holidays = process_holidays(
    holidays
)

weather = process_weather(
    weather
)

final_df = merge_data(
    products,
    holidays,
    weather
)

# Normalize object columns (nested structures, bytes, NaN) to strings
obj_cols = final_df.select_dtypes(include=["object"]).columns
if len(obj_cols) > 0:
    for c in obj_cols:
        final_df[c] = final_df[c].apply(
            lambda x: json.dumps(x) if isinstance(x, (dict, list, tuple, set))
            else (x.decode('utf-8') if isinstance(x, (bytes, bytearray)) else ("" if pd.isna(x) else x))
        )

quality_report = {

    "records": len(final_df),

    "columns": len(final_df.columns),

    "missing_values":
        final_df.isnull().sum().sum(),

    "duplicates":
        final_df.duplicated().sum()
}
print(quality_report)

final_df.to_parquet(
    "data/processed/retail_features.parquet",
    index=False
)

