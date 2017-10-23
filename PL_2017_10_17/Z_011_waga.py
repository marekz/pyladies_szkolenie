# Napisz funkcję, która znajdzie liczbę odważników o wadze A aby zrównoważyć szale wagi z odważnikami o wadze B.
# Przykład działania: >>> odwazniki(2, 8) 4, 1 >>> odwazniki(4, 6) 3, 2

def wyszukajMaxWspolna(a, b):
    tmpA = 1
    wskaznikB = 1
    tmpB = 1
    tmpBT = []

    for licznik in range(10):
        tmpA = a * licznik
        if tmpA >= wskaznikB:
            wskaznikB = wskaznikB + 1
            tmpB = b * wskaznikB
            tmpBT.append(tmpB)

            for element in tmpBT:
                if (element % a == 0):
                    return element



def odwazniki(odwaznikA, odwaznikB):

    lista = []

    if odwaznikB % odwaznikA == 0:
        lista.append(int(odwaznikB/odwaznikA))
        lista.append(1)
        print(lista)

    else:
        wspolna = wyszukajMaxWspolna(odwaznikA, odwaznikB)
        a = int(wspolna/odwaznikA)
        b = int(wspolna/odwaznikB)
        lista.append(a)
        lista.append(b)
        print(lista)

odwazniki(2, 8)
odwazniki(4, 6)
odwazniki(3, 5)