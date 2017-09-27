# Napisz funkcję która sprawdzi czy dana liczba jest liczbą brzydką.
# Liczby brzydkie, to takie które są podzielen przez 2, 3 lub 5
# Liczba 1 jest również liczbą brzydką
#
# Przykłąd:
# input: ugly(12)
# output: True
# input: ugly(11)
# output: False

def sprawdzLiczbe(liczba):
    status = False
    if liczba%2==0 or liczba%3==0 or liczba%5==0 or liczba==1:
        status = True
    return status

def wyswietlStatusLiczby(statusLiczby):
    if statusLiczby==True:
        infoString = "Brzydka liczba :)"
    else:
        infoString = "Ładna liczba :)"

    return infoString

graRazJeszcze = True

while graRazJeszcze:

    liczba = int(input("Podaj liczbę do sprawdzenia: "))
    statusLiczby = sprawdzLiczbe(liczba)

    print(wyswietlStatusLiczby(statusLiczby))

    if "N" == input("Czy chcesz raz jeszcze T/N "):
        graRazJeszcze = False

# TODO: dopisać wyjątki w przypadku wprowadzenie błędnych danych