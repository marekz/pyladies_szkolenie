from random import randint

# Lista słów
listaSlow = ['kaszmir', 'kalisz', 'rabarbar', 'trabant', 'kozak', 'grzechotka', 'szczecin', 'wieloryb', 'matematyka',
             'śwetlik', 'samochód', 'motocyklista', 'nocnik', 'wachacz', 'wąsacz', 'literat', 'perkusja', 'radość',
             'przyjemność', 'łącznik', 'piórnik', 'marketer', 'ciągnik', 'rumcajs', 'żyrafa', 'krokodyl', 'kameleon']

# Pobranie liczby słów z listy
listaSlowLength = len(listaSlow)

czyRazJeszcze = True

while czyRazJeszcze:

    # Wygenerowanie losowego słowa tablicy
    idSlowa = randint(0, listaSlowLength - 1)

    wylosowano = listaSlow[idSlowa]
    wylosowaneSlowo = list(wylosowano)

    # pobranie długości słowa
    dlugoscSlowa = len(wylosowaneSlowo)

    # przysłonięcie listy słów znakami * np: "kot" ***
    przesloniete = "*" * dlugoscSlowa
    przeslonieteSlowo = list(przesloniete)

    # start gry

    print(przesloniete)
    # print(przeslonieteSlowo)

    # Inicjacja licznika
    licznik = 0
    # prośba do użytkownika o podanie literki

    licznikProb = 0

    czyPowtarzac = True

    while czyPowtarzac:

        wprowadzonaLitera = input("Podaj znak do porównania: ")

        if wprowadzonaLitera == "exit":
            czyPowtarzac = False
            czyRazJeszcze = False
        else:
#sprawdzenie czy literka występuje w wyrazie
            if wprowadzonaLitera == wylosowano:
                print("Zgadłeś! Wylosowany wyraz to {0}".format(wylosowano))
                czyPowtarzac = False

            elif wprowadzonaLitera in wylosowaneSlowo:
#jeśli występuje, odsłonięcie literki,
                licznik = 0
                indexZnakuWWyrazie = []
                for znak in wylosowaneSlowo:
                    if znak == wprowadzonaLitera:
                        przeslonieteSlowo[licznik] = wprowadzonaLitera
                    licznik += 1
#Wyświetlenie przesłoniętego wyrazu
                print("".join(przeslonieteSlowo))
            else:
#jeśli nie wyświetlenie informacji o nieudanej próbie
                print("Znak {0} nie występuje w wyrazie {1}".format(wprowadzonaLitera, "".join(przeslonieteSlowo)) )
#powiększenie licznika kroków
            licznikProb += 1

#powtarzanie kroków do chwili odsłonięcia wszystkich liter,
            if "*" not in przeslonieteSlowo:
                czyPowtarzac = False
#wyświetlenie statystyki gry i wyjście z programu
    print("Prób {0}".format(licznikProb))

    if "n" == input("Grasz raz jeszcze?: "):
        czyRazJeszcze = False