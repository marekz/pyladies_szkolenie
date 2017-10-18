from builtins import print

def cenzura_cyfr(slowo):

    hash_znak = ''

    for znak in slowo:
        try:
            new_znak = int(znak)
        except:
            new_znak = znak

        if type(new_znak) is int:
            hash_znak = hash_znak + "#"
        else:
            hash_znak = hash_znak + new_znak

    return hash_znak

slowo = input("Wprowadź slowo do zakodowania: ")
print(cenzura_cyfr(slowo))
print(cenzura_cyfr("password12345"))
print(cenzura_cyfr("a1a ma k0ta"))
