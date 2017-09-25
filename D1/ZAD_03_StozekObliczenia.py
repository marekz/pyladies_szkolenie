print("Obliczanie stożka");
r_promienPodstawy  = float(input("Podaj promień podstawy: "));
l_tworzaca_stozek  = float(input("Podaj tworzącą stożek: "));
h_wysokosc_stozka  = float(input("Podaj wysokość stożka"));

# (PI* r ^ 2 * H) /3

objetosc_storzka = (3.14 * h_wysokosc_stozka * r_promienPodstawy ** 2) / 3;