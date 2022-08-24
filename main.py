import requests


def getData(url):
    request = requests.get(url).json()
    data = request["results"]

    while request["next"]:
        request = requests.get(request["next"]).json()
        data += request["results"]
    return data


planetas = requests.get("https://swapi.dev/api/planets/").json()

aridos = 0
for planeta in planetas["results"]:
    if (planeta["climate"] == "arid"):
        aridos += len(planeta["films"])

print(f'hay {aridos} planetas donde su clima es arido')


personas = getData("https://swapi.dev/api/people/")
count = 0
wookies = []
for persona in personas:
    if len(persona["species"]) > 0:
        if persona["species"][0] == "https://swapi.dev/api/species/3/":
            wookies.append((persona["name"]))
            for film in persona["films"]:
                if film == "https://swapi.dev/api/films/6/":
                    count += 1

print(f"En la Sexta Pelicula de StarWars hay {count} wookies y se llaman {wookies[0]} y {wookies[1]}")


naves = getData("https://swapi.dev/api/starships/")
i = 0
tamanos = []
for nave in naves:
    try:
        if nave["length"] != "unknown":
            tamanos.append(float(nave["length"]))
    except ValueError:
        pass

target = (max(tamanos))

for nave in naves:
    try:
        if nave["length"] != "unknown":
            if float(nave["length"]) == target:
                Nave = nave["name"]
                size = nave["length"]
    except ValueError:
        pass

print(f'La {Nave} es la aeronave mas grande y mide {size}')
