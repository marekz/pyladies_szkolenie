def policz_samogloski(zdanie):
    samogloski = ['a','e','i','o','u']
    licznik = 0
    for letter in zdanie:
        if letter in samogloski:
            licznik = licznik +1
    return licznik

print(policz_samogloski("Ala ma kota"))
print(policz_samogloski("Pies psu niedzwiedziem"))
