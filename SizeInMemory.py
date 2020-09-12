import sys
import decimal
from Person import Person

print("An Integer:")
i = int(100)
print(sys.getsizeof(i))

print("Empty String:")
emptyString = ""
print(sys.getsizeof(emptyString))

print("A Normal String:")
s = "Hello World"
print(sys.getsizeof(s))

print("Increasing String:")
for i in range(0,5):
    emptyString = emptyString + chr(i)
    print(sys.getsizeof(emptyString))
    
print("Empty Dictionary:")
dict1 = {}
print(sys.getsizeof(dict1))

print("Dictionary with Key:")
dict1["Key"] = "value1"
print(sys.getsizeof(dict1))

print("Set:")
set1 = set()
print(sys.getsizeof(set1))

print("Basic Class:")
f = Person()
print(sys.getsizeof(f))

class DerivedPerson(Person):
    def __init__(self):
        Person.__init__(self)
        
print("Derived Class:")
dp = DerivedPerson()
print(sys.getsizeof(dp))

print("Decimal:")
d = decimal.Decimal()
print(sys.getsizeof(d))

print("List:")
l = list(range(1,6))
print(sys.getsizeof(l))

print("List2:")
l2 = [decimal.Decimal(100), decimal.Decimal(200)]
print(sys.getsizeof(l2))