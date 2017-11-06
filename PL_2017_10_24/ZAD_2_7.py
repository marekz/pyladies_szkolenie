# 2.7 Wczytaj zawarty w pliku json.
# Stwórz plik który będzie posiadał wszystkie statki w zdaniach od najdroższego do najtańszego:
# <Nazwa> kosztuje <123> credits.

import json

with open("py1.2zd.json","r") as file:
    ship_data = json.load(file)

unknown = []
toSorted = []

for element in ship_data:
    if element['cost_in_credits'] == 'unknown':
        slo = {}
        slo = {'nazwa': element['starship_class'], 'cost': 'unknown'}
        unknown.append(slo)
    else:
        slo = {}
        slo = {'nazwa': element['starship_class'], 'cost': int(element['cost_in_credits'])}
        toSorted.append(slo)

sortedCrafts = sorted(toSorted, key=lambda ship : ship['cost'])

allCrafts = sortedCrafts + unknown

newFile = "SortedShip.txt"
mode = "w"

openTOWrite = open(newFile, mode)

for element in allCrafts:
    openTOWrite.write('{0} kosztuje {1} credits.\n'.format(element['nazwa'],element['cost']))