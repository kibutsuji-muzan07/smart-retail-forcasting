import httpx
import pandas as pd
import os, sys
sys.path.insert(0, os.getcwd())

from etl.utils.logger import logger
from etl.utils.retry_handler import retry_api
from etl.utils.config_loader import load_config
from configs.settings import build_url

config = load_config()

@retry_api()
def fetch_holidays():

    url = build_url('holiday_api', 'holidays')

    logger.info(f"Fetching holidays from {url}")

    response = httpx.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)

    logger.info(f"Fetched {len(df)} holidays")

    df.to_json(
        "data/raw/holidays/holidays.json",
        orient="records",
        indent=4
    )

    return df