# Zadanie 3
# Napisz funkcję która spłaszczy strukturę zagnieżdżonych list do płaskiej listy:
# Np:
# Input: flatten([[[[[[[[[['a']'b']]]'c']]]'d']]'e'])
# Output: ['a','b','c','d','e']
#
from builtins import len, type

def addElementToLIst(element):
    normalList.append(element)

def newList(listElement):

    for element in listElement:

        if type(element) is list:
            newList(element)
        else:
            addElementToLIst(element)

strangeList = [[[[[[[[[['a'],'b']]],'c']]],'d'],'f',['g','h']],'e']
normalList = []

newList(strangeList)

print(normalList)