# Napisz funkcję, która policzy drogę pokonaną przez samochód w czasie t i przyspieszeniu a z opcjonalną prędkością początkową, domyślnie równą 0. >>> droga(5, 5) 62.5 >>> droga(10, 10, vs=100) 1500

def droga(czas, przyspieszenie, predkoscPoczatkowa = 0):
    droga = ((predkoscPoczatkowa * czas) + ((przyspieszenie * czas * czas)/2))
    return droga

print(droga(10, 10, 100))
print(droga(5,5))