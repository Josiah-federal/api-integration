import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    print("❌ ERROR: Weather API key not found in .env")
    exit(1)

# ---------------- CRYPTO FUNCTION ----------------
def fetch_crypto_price(crypto_id, currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto_id,
        "vs_currencies": currency
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        if crypto_id not in data:
            print(f"❌ Error: Cryptocurrency '{crypto_id}' not found.")
            return None

        return data[crypto_id][currency]

    except Exception as e:
        print(f"❌ Crypto API error: {e}")
        return None

# ---------------- WEATHER FUNCTION ----------------
def fetch_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return temp, description

    except Exception as e:
        print(f"❌ Weather API error: {e}")
        return None

# ---------------- MAIN FUNCTION ----------------
def main():
    crypto = input("Enter cryptocurrency (bitcoin, ethereum, etc.): ").lower()
    city = input("Enter your city: ")

    crypto_price = fetch_crypto_price(crypto)
    weather = fetch_weather(city, WEATHER_API_KEY)

    print("\n📊 Live Information")
    print("-" * 30)

    if crypto_price is not None:
        print(f"💰 {crypto.capitalize()} Price: ${crypto_price}")

    if weather is not None:
        temp, description = weather
        print(f"🌤️ Weather in {city.capitalize()}: {temp}°C, {description}")

if __name__ == "__main__":
    main()
