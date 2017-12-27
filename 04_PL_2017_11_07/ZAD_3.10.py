# Korzystając z API https://swapi.co/api/.
# Wyświetl imiona wszytkich Gunganów w języku Wooki.

import requests
from pprint import pprint as pp

url = 'https://swapi.co/api/people/?format=wookiee'

inhabitant_data = []
nextRecord = ''
error_log = []

def getHomeworld(url):
    return getRequest(url);

def iterateResult(results):
    for element in results:
        try:
            species = element['species'][0]
        except IndexError:
            error_log.append("IndexError")

        person = getRequest(species)
        # name = element['name']
        # species = getHomeworld(element['species'])
        # print(species)
        if person['name'] == 'Gungan':
            print(person)
            # print(person['name'])
            # inhabitant_data.append(element)

def getRequest(url):
    resp = requests.get(url)
    data = resp.iter_content()
    # pp(data)

    for element in data:
        print(element)


    # pp(data)
    # try:
    #     if data['results']:
    #         results = data['results']
    #         iterateResult(results)
    # except KeyError:
    #     error_log.append("Brak pola result")
    #
    # try:
    #     if data['next']:
    #         getRequest(data['next'])
    # except KeyError:
    #     error_log.append("Brak następnego rekordu")
    #
    # return data

api_swapi = getRequest(url)
# data_people = getRequest(api_swapi['people'])

# pp(inhabitant_data)