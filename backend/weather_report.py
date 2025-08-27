from pydantic_ai import Agent
from pydantic import BaseModel
from dotenv import load_dotenv
import requests, os, json
from typing import List

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATER_API_KEY")

class WeatherQuery(BaseModel):
    location: str
    dates: List[str]

agent = Agent("openai:gpt-4o-mini")

class WeatherReport(BaseModel):
    location: str
    date: str  
    temperature_celsius: float
    condition: str
    humidity: int
    wind_kph: float

def fetch_weather(location: str, target_dates: List[str]) -> List[WeatherReport]:
    reports = []

    # Forecast endpoint
    forecast_url = "http://api.weatherapi.com/v1/forecast.json"
    forecast_params = {"key": WEATHER_API_KEY, "q": location, "days": 10}
    forecast_resp = requests.get(forecast_url, params=forecast_params).json()

    # Check if API returned error
    if "error" in forecast_resp:
        print("API error:", forecast_resp["error"]["message"])
        return []

    forecast_days = forecast_resp["forecast"]["forecastday"]
    loc_name = forecast_resp["location"]["name"]

    for date in target_dates:
        report_data = None

        # Check if date is in forecast
        for day in forecast_days:
            if day["date"] == date:
                report_data = day
                break

        # If date not in forecast, use history endpoint
        if not report_data:
            history_url = "http://api.weatherapi.com/v1/history.json"
            history_params = {"key": WEATHER_API_KEY, "q": location, "dt": date}
            history_resp = requests.get(history_url, params=history_params).json()

            if "error" in history_resp:
                print(f"API error for date {date}: {history_resp['error']['message']}")
                continue

            report_data = history_resp["forecast"]["forecastday"][0]

        # Build structured WeatherReport
        reports.append(
            WeatherReport(
                location=loc_name,
                date=report_data["date"],
                temperature_celsius=report_data["day"]["avgtemp_c"],
                condition=report_data["day"]["condition"]["text"],
                humidity=report_data["day"]["avghumidity"],
                wind_kph=report_data["day"]["maxwind_kph"],
            )
        )

    return reports


nlq = input("What do you know about weather: ")
strict_prompt = f"""
Extract the weather query from the user's request.
Return ONLY JSON, nothing else, no text, no markdown, not even a single work extra.
most importtantly convert the date into YYYY-MM-DD format.
if the user provide date as today or tomorrow or yesterday convert it to the actual date.
JSON schema:
{json.dumps(WeatherQuery.model_json_schema(), indent=2)}

User request: "{nlq}"
"""
result = agent.run_sync(strict_prompt)
parsed_json = result.output.strip()  
query = WeatherQuery.model_validate_json(parsed_json)
reports = fetch_weather(query.location, query.dates)

# for report in reports:
#     print(report.model_dump_json(indent=2))


def json_report_to_nlq(reports: List[WeatherReport]) -> str:
    if not reports:
        return "No weather data available."

    summary = f"Weather report for {reports[0].location}:\n"
    for report in reports:
        summary += (
            f"Date: {report.date}\n"
            f"Temperature: {report.temperature_celsius}°C\n"
            f"Condition: {report.condition}\n"
            f"Humidity: {report.humidity}%\n"
            f"Wind: {report.wind_kph} kph\n\n"
        )
    return summary
print(json_report_to_nlq(reports))
