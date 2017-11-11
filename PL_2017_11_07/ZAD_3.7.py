# Korzystając z API https://swapi.co/api/. Pobierz dane wszystkich mieszkańców planety Tatooin

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


url = 'https://swapi.co/api/'
resp = requests.get(url)

api_swapi = resp.json()

url_api_people = api_swapi['people']

resp = requests.get(url_api_people)
data_people = resp.json()

from pprint import pprint as pp

pp(data_people['next'])
pp(data_people['results'])
pp(data_people)


# print(api_people)