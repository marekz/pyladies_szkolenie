# 2.6 Zapisz plik sw_all_heros z bohaterami w zdaniach:
# <Imie> wazy <waga> kg jest <plec> i pochodzi z <Planeta>.
# Przykład: Anakin Skywakaer waży 90 kg jest mężczyzną i pochodzi z Tatuin.

import json

def save_hero_to_files():
    for element in JSONFile:
        imie = element['name']
        waga = element['mass']
        plec = element['gender']
        planeta = element['homeworld']

        if plec == 'male':
            plec = "mężczyzną"
        elif plec == 'female':
            plec = 'kobietą'
        save_string = "{0} wazy {1} kg jest {2} i pochodzi z {3}.\n".format(imie, waga, plec, planeta)

        saveFile = open('sw_all_heros', 'a')
        saveFile.write(save_string)

file = "py1.2.json"
mode = "r"

fileOpen = open(file, mode)

JSONFile = json.load(fileOpen)

save_hero_to_files()


