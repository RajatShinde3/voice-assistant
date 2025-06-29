import requests
import os

# Load your API key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> str:
    """
    Fetches weather data for the given city using OpenWeatherMap API.
    Returns a short spoken-style weather report.
    """
    if not API_KEY:
        return "Weather service is not configured. Please set your API key."

    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "main" not in data:
            return f"Sorry, I couldn't get the weather for {city}."

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        condition = data["weather"][0]["description"].capitalize()

        return (
            f"The current weather in {city.title()} is {condition}, "
            f"with a temperature of {temp} degrees Celsius. "
            f"It feels like {feels_like} degrees."
        )

    except Exception as e:
        return f"Failed to get weather: {str(e)}"
