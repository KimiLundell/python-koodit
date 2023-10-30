import requests
kunta = input("Syötä paikkakunta: ")
haku = ("https://api.openweathermap.org/data/2.5/weather?q=" + kunta +
        ",fi&appid=2b53c678548afac76ada173f1825e21c&lang=fi")
try:
    vastaus = requests.get(haku)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["weather"][0]["description"])
        celsius = (json_vastaus["main"]["temp"]) - 273.15
        print(f"{celsius:.1f}°c")
    else:
        print("Kuntaa ei löydy.")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
