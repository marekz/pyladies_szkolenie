# Napisz funkcję, która policzy wszystkie samogłoski w tekście. Przykład działania >>> policz_samogloski("Ala ma kota") 5 >>> policz_samogloski("Pies psu niedzwiedziem") 9

def policz_samogloski(zdanie):
    samogloski = ["a","e","i","o","u"]
    licznik = 0
    for letter in zdanie:
        if letter in samogloski:
            licznik = licznik +1
    return licznik

print(policz_samogloski("Ala ma kota"))
print(policz_samogloski("Pies psu niedzwiedziem"))
