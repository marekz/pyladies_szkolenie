def policz_slowa(zdanie):
    liczba_elementow = 1
    for letter in zdanie:
        if letter == ' ':
            liczba_elementow = liczba_elementow + 1
    return liczba_elementow

print(policz_slowa("Ala ma kota"))
print(policz_slowa("Pies psu niedzwiedziem, bo tak"))