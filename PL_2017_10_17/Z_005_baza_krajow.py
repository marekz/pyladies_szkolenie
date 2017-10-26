# Korzystając w ze ściągniętego pliku z bazą krajów. Wyświetl wszystkie kraje w Ameryce Północnej. (Northern America).

from countries import *

def showCountries(subregion):

    for element in countries:
        if element["subregion"] == subregion:
            print(element["name"]["official"])

showCountries("Northern America")