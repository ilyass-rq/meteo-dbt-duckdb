# fiche = {"nom": "paris", "lat": 48.85}
# print(fiche["nom"])
# print(fiche["lat"])


# villes = ["paris", "lyon", "marseille"]
# for ville in villes:
#     print("ville :", ville)


villes = [{"nom": "paris","lat": 48.85 },{"nom": "lyon", "lat":69.2}]
for v in villes:
    print(v["nom"],v["lat"])
 

# dates = data["daily"]["time"]
# temp_max = data["daily"]["temperature_2m_max"]
# temp_min = data["daily"]["temperature_2m_min"]
# lignes = []
# for date, tmax, tmin in zip(dates,temp_max,temp_min):
#     lignes.append({"ville": ville, "date":date, "temperature_max":tmax,"temperature_min":tmin})
# print(lignes)