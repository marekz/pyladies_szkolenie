# Napisz funkcję, która zamieni czas (HH:MM:SS) na
# sekundy, minuty, godziny.
# Przykład:
# Input : get_time(’2:00:00’, ’s’)
# Output : 7200
# Input : get_time(’12:00:00’, ’m’)
# Output : 720
# Input : get_time

# Wyświetl informacje o akceptowalnych datach

import string

print("############################################################")
print("# Funkcja zmieniająca czas na sekundy, minuty bądz godziny #")
print("# np:                                                      #")
print("# Input : get_time('2:00:00', 's')                         #")
print("# Output : 7200                                            #")
print("# Input : get_time(’12:00:00’, ’m’)                        #")
print("# Output : 720                                             #")
print("# Przeliczanie wykonać pomijając funkcje data              #")
print("############################################################")

def expandTimeStringToSeconds(dataString):
    dataArray = dataString.split(":")
    seconds = 60*60* int(dataArray[0]) + 60 * int(dataArray[1]) + int(dataArray[2])

    return seconds

def getTime(dataString, method):

    seconds = expandTimeStringToSeconds(dataString)

    if method == 's':
        message = "Podany format zawiera {0} sekund".format(seconds)
    elif method == 'm':
        message = "Podany format zawiera {0} minut".format(seconds/60)
    elif method == 'h':
        message = "Podany format zawiera {0} godzin".format(seconds / 3600)
    else: message = "Zły wybór"

    return message

again = True
while again:


    time            = input("Wprowadź jednostkę czasu do przeliczenia w powyższych przykładów: ")
    print("Wprowadź jednostkę do której chcesz przeliczyć [s]: sekunda, [m]: minuta, [h]: godzina")
    calculateTo     = input("Wybór: ")

    print(getTime(time, calculateTo))

    askAgain = input("Czy raz jeszcze? [T/N]")
    if askAgain == "N":
        again = False

# TODO: Pobawić się w wyjątki