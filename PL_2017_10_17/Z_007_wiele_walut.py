# Korzystając w ze ściągniętego pliku z bazą krajów. Wyświetl wszystkie kraje, które mają więcej niż jedną walutę (currency) oraz wypisz te waluty.
from countries import *

def showCountries():

    for element in countries:
        liczba_walut = len(element["currency"])
        if liczba_walut > 1:
            print("Kraj: " + element["name"]["official"] + " ma następujące waluty: ")
            for waluta in element["currency"]:
                print(" - " + waluta)

showCountries()