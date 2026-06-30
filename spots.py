# spots.py

SPOTS = [

    {
        "name": "Klitmøller",

        "lat": 57.044,
        "lon": 8.494,

        # Hard Rules
        "min_period": 12.0,
        "min_height": 0.5,
        "min_session": 3,

        "max_onshore": 5.0,
        "max_offshore": 8.0,

        # Ideale Richtungen
        "ideal_swell": 315,
        "ideal_wind": 110,

        # Gewichtungen
        "weight_period": 0.30,
        "weight_height": 0.25,
        "weight_wind": 0.30,
        "weight_tide": 0.15,
    },

    {
        "name": "Nørre Vorupør",

        "lat": 56.957,
        "lon": 8.371,

        "min_period": 11.5,
        "min_height": 0.6,
        "min_session": 3,

        "max_onshore": 5,
        "max_offshore": 8,

        "ideal_swell": 315,
        "ideal_wind": 110,

        "weight_period": 0.30,
        "weight_height": 0.25,
        "weight_wind": 0.30,
        "weight_tide": 0.15,
    }

]
