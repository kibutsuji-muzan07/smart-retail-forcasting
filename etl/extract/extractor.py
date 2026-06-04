from product_api import fetch_products
from holiday_api import fetch_holidays
from weather_api import fetch_weather

def run_extractors():

    products = fetch_products()
    holidays = fetch_holidays()
    weather = fetch_weather()

    print(products.head())
    print(holidays.head())
    print(weather.head())

if __name__ == "__main__":
    run_extractors()