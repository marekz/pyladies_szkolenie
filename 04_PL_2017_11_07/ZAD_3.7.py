# Korzystając z API https://swapi.co/api/. Pobierz dane wszystkich mieszkańców planety Tatooine

# GET /api/
#
# HTTP 200 OK
# Allow: GET, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "people": "https://swapi.co/api/people/",
#     "planets": "https://swapi.co/api/planets/",
#     "films": "https://swapi.co/api/films/",
#     "species": "https://swapi.co/api/species/",
#     "vehicles": "https://swapi.co/api/vehicles/",
#     "starships": "https://swapi.co/api/starships/"
# }

import requests
from pprint import pprint as pp

url = 'https://swapi.co/api/'

inhabitant_data = []
nextRecord = ''
error_log = []

def getHomeworld(url):
    return getRequest(url);

def iterateResult(results):
    for element in results:
        name = element['name']
        homeworld = getHomeworld(element['homeworld'])
        if homeworld['name'] == 'Tatooine':
            inhabitant_data.append(element)

def getRequest(url):
    resp = requests.get(url)
    data = resp.json()

    try:
        if data['results']:
            results = data['results']
            iterateResult(results)
    except KeyError:
        error_log.append("Brak pola result")

    try:
        if data['next']:
            getRequest(data['next'])
    except KeyError:
        error_log.append("Brak następnego rekordu")

    return data

api_swapi = getRequest(url)
data_people = getRequest(api_swapi['people'])

pp(inhabitant_data)