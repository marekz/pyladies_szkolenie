# for a in range(10):
#     galazka = ' ' * (10 - a) + '/' * a + '\\' * a
#     print(galazka)

for a in range(10):
    galazka_lewa = ' ' * (10 - a) + '/' * a
    galazka_prawa = '\\' * a
    print(galazka_lewa + galazka_prawa)