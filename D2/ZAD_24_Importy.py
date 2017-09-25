from random import randint

tryb = input("Wybierz tryb gry: [h]-hard/[s]-soft: ")

if tryb == "h":
    maxrand = 1000
else:
    maxrand = 100

playAgain = True
while playAgain:

    wylosowana = randint(1, maxrand)
    print(wylosowana)
    result = True

    while result:
        wprowadzona = int(input("Podaj wartość: "))
        if (wprowadzona == wylosowana):
            print("Bingo")
            result = False
        elif (wprowadzona < wylosowana):
            print("Za mała")
        elif (wprowadzona > wylosowana):
            print("Za duża")
    playQuery = input("Chcesz zagrać raz jeszcze?")
    if playQuery == 'n':
        playAgain = False
