class AnObject():
    def __init__(self):
        self.listOfIntegers = [1,2,3,4]
        self.dictionaryElement = {
            'a': 1,
            'b': 2
        }
    
    def printMe(self):
        print(self.listOfIntegers)
        print(self.dictionaryElement)
        
a = AnObject()
a.listOfIntegers.append(5)
a.printMe()

b = a
b.listOfIntegers.append(6)
b.printMe()
a.printMe()

import copy

print("Shallow copy")
c = copy.copy(a)
c.listOfIntegers.append(7)
c.printMe()
a.printMe()

print("Deep Copy")
d = copy.deepcopy(c)
d.listOfIntegers.append(8)
d.printMe()
c.printMe()