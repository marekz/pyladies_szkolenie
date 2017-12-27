# Korzystając w ze ściągniętego pliku z bazą krajów. Znajdź kraj, który graniczy z największą ilością innych krajów (borders) i wyświetl jego nazwę oraz ilość granic

from countries import *

def showParameters():

    number_of_borders = 0
    selected_country = ""

    for element in countries:
        if len(element["borders"]) > number_of_borders:
            selected_country = element["name"]["official"]
            number_of_borders = len(element["borders"])
            name_borders = element["borders"]

    print("""Kraj o nwjwiększej liczbie sąsiadów to: {0}. {0} ma {1} sąsiadów. Sąsiedzi to: {2}""". format(selected_country, number_of_borders, name_borders))

showParameters()
