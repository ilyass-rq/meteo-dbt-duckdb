import requests
url = "https://archive-api.open-meteo.com/v1/archive"

params = {

    "latitude":48.85,
    "longitude":2.34,
    "start_date":"2026-10-01",
    "end_date":"2026-10-07",
    "daily":"temperature_2m_max,temperature_2m_min",
    "timezone":"Europe/Paris"
}

response = requests.get(url, params=params)
print(response.url)

data=response.json()
print(data["daily"])