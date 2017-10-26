# Napisz funkcję, która policzy słowa w tekście. Każde słowo jest oddzielone spacją. Przykład działania >>> policz_slowa("Ala ma kota") 3 >>> policz_slowa("Pies psu niedzwiedziem, bo tak") 5

def policz_slowa(zdanie):
    liczba_elementow = 1
    for letter in zdanie:
        if letter == " ":
            liczba_elementow = liczba_elementow + 1
    return liczba_elementow

print(policz_slowa("Ala ma kota"))
print(policz_slowa("Pies psu niedzwiedziem, bo tak"))