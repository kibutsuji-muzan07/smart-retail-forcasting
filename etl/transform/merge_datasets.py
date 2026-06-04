def merge_data(
        products,
        holidays,
        weather
):

    products["holiday_count"] = len(
        holidays
    )

    products["is_hot"] = (
        weather.iloc[0]["is_hot"]
    )

    products["is_humid"] = (
        weather.iloc[0]["is_humid"]
    )

    return products