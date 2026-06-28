import os, sys
import django
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.settings"
)

django.setup()

from inventory.models import ProductAnalytics

df = pd.read_parquet(
    Path.joinpath(BASE_DIR, "data/processed/retail_features.parquet")
)

def load_products():

    objects = []

    for _, row in df.iterrows():

        objects.append(

            ProductAnalytics(

                product_id=row["id"],

                title=row["title"],

                category=row["category"],

                price=row["price"],

                stock=row["stock"],

                inventory_value=row["inventory_value"],

                is_hot=row["is_hot"],

                humidity=row["is_humid"],

                holiday_count=row["holiday_count"]
            )
        )

    ProductAnalytics.objects.bulk_create(
        objects
    )

    print(
        f"{len(objects)} rows loaded."
    )

if __name__ == "__main__":
    load_products()