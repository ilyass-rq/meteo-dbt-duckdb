import requests
import json
import duckdb

url = "https://archive-api.open-meteo.com/v1/archive"

villes = [
    {"nom": "paris", "lat": 48.85, "lon": 2.34},
    {"nom": "lyon", "lat": 45.76, "lon": 4.84},
    {"nom": "marseille", "lat": 43.30, "lon": 5.37}
]


con = duckdb.connect("meteo.duckdb")
con.execute("CREATE TABLE IF NOT EXISTS raw_meteo (ville varchar, payload JSON,loaded_at timestamp )")

for v in villes:


    params = {

        "latitude":v["lat"],
        "longitude":v["lon"],
        "start_date":"2026-10-01",
        "end_date":"2026-10-07",
        "daily":"temperature_2m_max,temperature_2m_min",
        "timezone":"Europe/Paris"
    }

    response = requests.get(url, params=params)
    data=response.json()
    con.execute("DELETE FROM raw_meteo WHERE ville = ?", [v["nom"]])
    con.execute("INSERT INTO raw_meteo VALUES (?,?,now())", [v["nom"], json.dumps(data),])

con.table("raw_meteo").show()
con.close()












