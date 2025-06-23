import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"\n📍 Weather in {city.title()}:")
            print(f"🌡️ Temperature: {temperature}°C")
            print(f"🌤️ Condition: {description}")
            print(f"💧 Humidity: {humidity}%")
            print(f"💨 Wind Speed: {wind_speed} m/s")
        else:
            print("❌ City not found. Please check the spelling and try again.")

    except Exception as e:
        print("⚠️ An error occurred:", e)


API_KEY = "Enter your weather app key here"

city = input("Enter your city name: ")
get_weather(city, API_KEY)
