# Korzystając z API https://swapi.co/api/.
# Policz BMI wszystkich pilotów Milenium Falcona I wyswietl je wraz z ich imionami.

import requests
from pprint import pprint as pp

url = "https://swapi.co/api/starships/"
error_log = []

species_list = []

def calculateBMI(height, mass):
    bmi = int(mass)/((int(height) / 100) ** 2)
    return bmi

def displayPilot(pilot):
    bmi = calculateBMI(pilot['height'], pilot['mass'])
    print("{0}, wzrost: {1}, masa {2}, BMI: {3}".format(pilot['name'], pilot['height'], pilot['mass'], bmi))

def showPilot(url):
    pilot = getRequest(url)
    displayPilot(pilot)

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