import requests


def load_forecast(lat, lon):

    url = "https://marine-api.open-meteo.com/v1/marine"

    params = {

        "latitude": lat,
        "longitude": lon,

        "hourly": ",".join([

            "wave_height",
            "wave_direction",
            "wave_period"

        ]),

        "forecast_days": 7,

        "timezone": "Europe/Berlin"

    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    print(response.url)

    response.raise_for_status()

    return response.json()
