# Wykorzystując dwie nowe wbudowane char() ord()
# >>> ord("a") 97 >>> chr(98) "b"
# funkcje zaimplementuj szyfr cezara, który jako drugi parametr będzie brał przesunięcie.
# Przykłady szyfr cezaraz o parametrze 3 podmieni każd literka alfabetu na trzecią z kolei np A na D a Z na C.
# >>> cezar("abc", 2) "cde"
# >>> cezar("abc", -2) "yza"
# Pamiętaj żeby znaki inne niż litery nie zmieniać.
# uwzględnij dodatkowo wielkie litery


small_a = ord("a")
small_z = ord("z")
big_a = ord("A")
big_z = ord("Z")
letter_number = small_z - small_a

def small_letter(letter, step):
    converted_sign = letter + step
    if converted_sign > small_z:
        converted_sign = (converted_sign - letter_number - 1)

    if converted_sign < small_a:
        converted_sign = (converted_sign + letter_number + 1)
    return converted_sign

def big_letter(letter, step):
    converted_sign = letter  + step
    if converted_sign > big_z:
        converted_sign = (converted_sign - letter_number - 1)

    if converted_sign < big_a:
        converted_sign = (converted_sign + letter_number + 1)

    return converted_sign

def replaceSign(sign, step):
    sign_in_int = ord(sign)

    if (sign_in_int >= small_a and sign_in_int <= small_z):
        operation = small_letter(sign_in_int, step)
    elif (sign_in_int >=big_a and sign_in_int <= big_z):
        operation = big_letter(sign_in_int, step)
    else:
        operation = sign_in_int

    return chr(operation)


def code_string(string, transfer):

    newString = ""

    for i in string:
        newString = newString + replaceSign(i, transfer)
    return newString

print(code_string("alamak 3 ąotaakotmaale", 1))