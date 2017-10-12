# Validacja kodu pocztowego
# Input: validate_zip('12-345')
# output: True
# Input: validate_zip('12345')
# output: False
# Input: validate_zip('12312-12312')
# output: False

def validate_zip(zip):

    status = True

    for letter in zip:
        print(letter)
    return status


print("Wprowadź kod pocztowy do walidacji:")
zip = input()

print(validate_zip(zip))
