# Korzystając w ze ściągniętego pliku z bazą krajów. Wyświetl wszystkie kraje niebędące w Afryce (Africa).
from countries import *

def showCountries(subregion):

    for element in countries:
        if element['region'] != subregion:
            print(element['name']['official'])

showCountries("Africa")