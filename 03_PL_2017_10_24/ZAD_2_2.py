# 2.2 Zapisz wszystkie osoby wyższe niż
# 200 cm do pliku hero_200_plus a resztę do pliku hero_short.

hero_200_plus = "hero_200_plus"
hero_short    = "hero_short"

def height_less(name):
    return True

def height_more(name):

    return True

def save_to_file(name, height):
    if int(height) > 200:
        filename = hero_200_plus
    else:
        filename = hero_short

    openedFile = open(filename, 'a')
    openedFile.write(name + " " + height + "\n")

filename = "py1.2.txt"
mode_access = "r"

file = open(filename, mode_access)

data = file.read()
dataArray = data.split('\n')

for element in dataArray:
    name = element[element.find('.')+2:element.find('has')].strip()
    height = element[element.find('and is ')+7:element.find('cm')].strip()

    save_to_file(name, height)