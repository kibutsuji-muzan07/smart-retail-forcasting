import httpx
import pandas as pd
import os, sys
sys.path.insert(0, os.getcwd())

from etl.utils.retry_handler import retry_api
from etl.utils.logger import logger
from configs.settings import build_url

@retry_api()
def fetch_products():

    url = build_url('product_api', 'products')
    logger.info(f"Fetching products from {url}")

    response = httpx.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    products = data['products']

    df = pd.DataFrame(products)

    logger.info(f"Fetched {len(df)} products")

    df.to_json(
        "data/raw/products/products.json",
        orient="records",
        indent=4
    )

    return df