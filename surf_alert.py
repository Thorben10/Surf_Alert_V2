from spots import SPOTS
from forecast import load_forecast
from telegram_bot import send


def main():

    print("=" * 60)
    print("Surf Alert V2 gestartet")
    print("=" * 60)

    for spot in SPOTS:

        print(f"\nPrüfe {spot['name']}...")

        try:

            forecast = load_forecast(
                spot["lat"],
                spot["lon"]
            )

            print("Forecast erfolgreich geladen.")

            hourly = forecast.get("hourly", {})

            waves = hourly.get("wave_height", [])

            if not waves:
                print("Keine Wellendaten vorhanden.")
                continue

            max_wave = max(waves)

            message = (
                f"🏄 {spot['name']}\n\n"
                f"Max. Wellenhöhe nächste 7 Tage:\n"
                f"{max_wave:.1f} m"
            )

            print(message)

            send(message)

        except Exception as e:

            print(e)


if __name__ == "__main__":
    main()
