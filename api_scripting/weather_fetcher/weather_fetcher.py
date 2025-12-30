import requests

city = input("Please enter a city: ").strip()

url = "https://geocoding-api.open-meteo.com/v1/search"
params = {
    "name": city,
    "count": 1,
    "language":"en",
    "format":"json"
}

response = requests.get(url,params=params,timeout=10)
response.raise_for_status()
data=response.json()
results = data.get("results")
if not results:
    print("City not found")
    exit
location = results[0]
lat = location["latitude"]
lon = location["longitude"]
name = location["name"]
country = location.get("country")

print(f"Found {name}, {country}")
print(f"Latitude: {lat}, Longitude {lon}")

forecast_url = "https://api.open-meteo.com/v1/forecast"

forecast_params = {
    "latitude": lat,
    "longitude":lon,
    "current": "temperature_2m,wind_speed_10m",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "auto"
}

forecast_response = requests.get(forecast_url,params=forecast_params,timeout=10)
forecast_response.raise_for_status()

forecast_data = forecast_response.json()

current = forecast_data.get("current", {})
daily = forecast_data.get("daily",{})

temp = current.get("temperature_2m")
wind = current.get("wind_speed_10m")

# Build lines of text for the report
lines = []
lines.append(f"Location: {name}, {country}")
lines.append(f"Latitude: {lat}, Longitude: {lon}")
lines.append("")
lines.append(f"Current temperature (°C): {temp}")
lines.append(f"Current wind speed (km/h): {wind}")
lines.append("")
lines.append("Next 5 days:")

dates = daily.get("time", [])
maxs = daily.get("temperature_2m_max", [])
mins = daily.get("temperature_2m_min", [])
rains = daily.get("precipitation_sum", [])

for i in range(min(5, len(dates))):
    day_line = (
        f"{dates[i]}  "
        f"max: {maxs[i]}°C  "
        f"min: {mins[i]}°C  "
        f"rain: {rains[i]} mm"
    )
    lines.append(day_line)

report_text = "\n".join(lines)

print()
print(report_text)

with open("weather_report.txt", "w") as f:
    f.write(report_text + "\n")

print("\nSaved to weather_report.txt")


