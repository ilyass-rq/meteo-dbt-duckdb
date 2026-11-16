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
# print(data["daily"]["temperature_2m_max"])


ville = "paris"
dates = data["daily"]["time"]
temp_max = data["daily"]["temperature_2m_max"]
temp_min = data["daily"]["temperature_2m_min"]
lignes = []
for date, tmax, tmin in zip(dates,temp_max,temp_min):
    lignes.append({"ville": ville, "date":date, "temperature_max":tmax,"temperature_min":tmin})
print(lignes)

