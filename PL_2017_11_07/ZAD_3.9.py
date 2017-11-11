# Korzystając z API https://swapi.co/api/.
# Policz BMI wszystkich pilotów Milenium Falcona I wyswietl je wraz z ich imionami.

import requests
from pprint import pprint as pp

url = "https://swapi.co/api/starships/"
error_log = []

species_list = []

def calculateBMI(pilot):

    print("Imię: {0}, Wysokość: {1}, Waga: {2}".format(pilot['name'], pilot['height'], pilot['mass']))
    # species = getRequest(species[0])
    #
    # if species['name'] not in species_list:
    #     species_list.append(species['name'])

def showPilot(url):
    pilot = getRequest(url)
    calculateBMI(pilot)

def iterateParts(results):
    for element in results:
        if element['name'] == 'Millennium Falcon':
            # pp(element)
            for part in element['pilots']:
                showPilot(part)

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

# print("Rasy występujące w V części Gwiezdnych Wojen: ")
# for elemement in species_list:
#     print(elemement)