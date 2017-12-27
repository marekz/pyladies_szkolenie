# Korzystając w ze ściągniętego pliku z bazą krajów. Wyświetl wszystkie kraje i ich stolice, jeśli stolica zaczyna się od litery W.

from countries import *

def showCountries():

    for element in countries:

        capital = element["capital"]

        if len(capital):
            if capital[0] == "W":
                print(element["name"]["official"])

showCountries()