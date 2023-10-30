import requests

haku = "https://api.chucknorris.io/jokes/random"
try:
    vitsi = requests.get(haku)
    if vitsi.status_code == 200:
        json_vitsi = vitsi.json()
        print(json_vitsi["value"])
except requests.exceptions.RequestException as i:
    print("Vitsiä ei voitu hakea.")
