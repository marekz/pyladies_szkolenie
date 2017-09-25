from math import pow

def dzialanie(a, b, d = "dodawanie"):
    if d == "dodawanie":
        c = a + b
        print("Wynikiem dodawania {0} + {1} jest: {2} ".format(a, b, c))
    elif d == "odejmowanie":
        c = a - b
        print("Wynikiem odejmowania {0} - {1} jest: {2} ".format(a, b, c))
    elif d == "mnożenie":
        c = a * b
        print("Wynikiem mnożenia {0} * {1} jest: {2} ".format(a, b, c))
    elif d == "dzielenie":
        c = a / b
        print("Wynikiem dzielenia {0} / {1} jest: {2} ".format(a, b, c))
    elif d == "potegowanie":
        c = pow(a,b)
        print("Wynikiem potegowania {0} do {1} jest: {2} ".format(a, b, c))
    else:
        print("Brak działania?")

dzialanie(10,2, "dzielenie")
dzialanie(20,12, "mnożenie")
dzialanie(4,8, "potegowanie")
