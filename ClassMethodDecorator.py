class Name:
    def __init__(self, first, middle, last):
        self._name = "{0} {1} {2}".format(first, middle, last)
    
    def name(self):
        return self._name

    @classmethod
    def fromFirstAndLast(self, first, last):
        self._name = "{0} {1}".format(first, last)
        return self._name
    
    @staticmethod
    def fromFirstAndMiddle(first, middle):
        return "{0} {1}.".format(first, middle)
    
n1 = Name("MyName", "MyMiddleName", "MySurname")
print("Standard: " + n1.name())

print("ClassMethod with Class: " + Name.fromFirstAndLast("MyName", "MySurname"))
print("ClassMethod with Ojbect: " + n1.fromFirstAndLast("MyName", "OtherMySurname"))
print("Object: " + n1.name())

print("Static with class: " + Name.fromFirstAndMiddle("MyName", "MyMiddleName"))
print("Static with object: " + n1.fromFirstAndMiddle("MyName", "OtherMyMiddleName"))
print("Object: " + n1.name())