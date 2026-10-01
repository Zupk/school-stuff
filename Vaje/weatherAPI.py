import requests
vreme = requests.get("https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1")
vremeJSON = vreme.json()
print(vremeJSON["latitude"])
print(vremeJSON["current"]["temperature_2m"])
