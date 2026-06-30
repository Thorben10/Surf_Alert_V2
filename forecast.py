import requests


def load_forecast(lat, lon):

    url = (
        "https://marine-api.open-meteo.com/v1/marine"
    )

    params = {

        "latitude": lat,
        "longitude": lon,

        "hourly":
        ",".join([

            "wave_height",
            "wave_direction",
            "wave_period",

            "wind_wave_height",
            "wind_wave_period",

            "wind_speed",
            "wind_direction"

        ]),

        "forecast_days": 7,
        "timezone": "Europe/Berlin"

    }

    r = requests.get(url, params=params, timeout=45)

    r.raise_for_status()

    return r.json()
