# Validacja adresu email
# Input: validate_email('piotr@dyba.com.pl')
# output: True
# Input: validate_email('piotrdyba.com.pl')
# output: False
# Input: validate_email('piotr@dyba')
# output: False

def validate_email(email):

    positionA = 0
    positionB = 0
    position = 0

    status = True

    for letter in email:
        if letter == '@':
            positionA = position
        elif letter == ".":
            positionB = position

        position = position + 1

    if positionB < positionA or positionB == 0 or positionA == 0:
        status = False

    return status


print("Wprowadź email do walidacji:")
email = input()

print(validate_email(email))
