from math import pow;


def policzBMI(waga, wzrost):
    bmi = round((float(waga) / pow((float(wzrost)) / 100, 2)), 2)
    if bmi <= 20:
        statusBMI = "niedowaga"
    elif bmi > 25:
        statusBMI = "nadwaga"
    else:
        statusBMI = "waga w normie"
    return statusBMI


def printInfo(result):
    print("Twój status: " + result)


def sprawdz_czy_cyfra():
    while True:
        try:
            return float(input("Podaj wartość: "))

        except ValueError:
            print("!!!!    Podaj liczbę    !!!!")


print("Wylicz BMI: ")
czy_kolejna = True

while czy_kolejna:

    print("Waga: ")
    waga = sprawdz_czy_cyfra()
    print("Wzrost: ")
    wzrost = sprawdz_czy_cyfra()

    result = policzBMI(waga, wzrost)
    printInfo(result)

    czy_nastepna = input("Wyjść z programu? ")
    if czy_nastepna == 't':
        czy_kolejna = False
