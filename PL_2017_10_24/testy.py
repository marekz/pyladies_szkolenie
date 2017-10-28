colorArray = ['red','blue','green','white']
print(colorArray)
newArray = {}

for color in colorArray:
    newArray[color] = []

print(newArray)


newArray['red'].append(100)
newArray['red'].append(34)
newArray['red'].append(12)
newArray['red'].append(65)
newArray['red'].append(23)
print(newArray)
