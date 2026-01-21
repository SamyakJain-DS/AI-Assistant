import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
today = datetime.date.today().isoformat()

def get_weather(city: str) -> str:
    """
    Fetches the current weather conditions for a given city.

    Use this tool when:
    - The task involves outdoor planning or daily scheduling
    - Temperature, rain, wind, or general weather conditions matter
    - You need context to decide between indoor vs outdoor activities

    Input:
    - city (str): Name of the city

    Output:
    - JSON containing temperature, weather description, humidity, wind, sunrise/sunset
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url).json()
    return res


def get_news(topic: str) -> list:
    """
    Fetches the latest news articles related to a topic or city.

    Use this tool when:
    - A situational awareness or daily briefing is required
    - Recent developments or headlines may affect the user's day
    - Only high-level summaries are needed, not deep analysis

    Input:
    - topic (str): Topic to search news for

    Output:
    - List of recent news articles with title, description, and URL
    """

    api_key = os.getenv("NEWS_API_KEY")
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&from={today}&to={today}"
        f"&pageSize=3&sortBy=publishedAt&apiKey={api_key}"
        )
    return requests.get(url).json().get("articles", [])


def get_events(city: str) -> dict:
    """
    Fetches upcoming local events for today and the near future.
    """
    api_key = os.getenv("SERPAPI_KEY")
    url = f"https://serpapi.com/search.json?engine=google_events&q=Events in {city}&api_key={api_key}"
    data = requests.get(url).json()

    filtered_events = data.get("events_results", [])

    data["events_results"] = filtered_events
    return data
