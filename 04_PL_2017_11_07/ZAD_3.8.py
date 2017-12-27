# Korzystając z API https://swapi.co/api/.
# Wyświetl wszystkie nazwy ras gatunków wystepujących w V częsci Gwiezdnych Wojen (Imperium kontratakuje).

import requests

url = "https://swapi.co/api/films"
error_log = []

species_list = []

def getSpecies(species):
    species = getRequest(species[0])

    if species['name'] not in species_list:
        species_list.append(species['name'])

def showCharacters(url):
    people = getRequest(url)
    getSpecies(people['species'])

def iterateParts(results):
    for element in results:
        if element['episode_id'] == 5:
            for part in element['characters']:
                showCharacters(part)

def getRequest(url):
    resp = requests.get(url)
    data = resp.json()

    try:
        if data['results']:
            results = data['results']
            iterateParts(results)
    except KeyError:
        error_log.append("Brak pola result")

    try:
        if data['next']:
            getRequest(data['next'])
    except KeyError:
        error_log.append("Brak następnego rekordu")

    return data

api_swapi = getRequest(url)

print("Rasy występujące w V części Gwiezdnych Wojen: ")
for elemement in species_list:
    print(elemement)