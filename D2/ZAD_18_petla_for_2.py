from pprint import pprint as pp

zliczacz = {}

wyraz = input('Podaj wyraz: ')

for let in wyraz:
    if let in zliczacz:
        zliczacz[let] += 1
    else:
        zliczacz[let] = 1
    print(zliczacz)
print(zliczacz)