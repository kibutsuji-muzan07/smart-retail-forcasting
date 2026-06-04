import httpx
import pandas as pd
import os, sys
sys.path.insert(0, os.getcwd())

from etl.utils.logger import logger
from etl.utils.retry_handler import retry_api
from configs.settings import build_url


@retry_api()
def fetch_weather():

    url = build_url('weather_api', 'current', city='Asansol', postal_code=713303)

    logger.info(f"Fetching weather for Asansol")

    response = httpx.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame([data])

    logger.info("Weather data fetched successfully")

    df.to_json(
        "data/raw/weather/weather.json",
        orient="records",
        indent=4
    )

    return df