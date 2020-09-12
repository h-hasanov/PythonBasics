x = [True, False, False]
print(any(x)) # prints True if there is at least one item in the Array True

# Anything that exists and is not 0 is True
x = [1,2,3,0]
print(all(x)) # as there is 0 in the array all returns False (as there is 1 False - 0)
x = [1,2,3,4]
print(all(x))

for idx, value in enumerate(x):
    print(idx,value)

dictionary = {"Element1":1, "Element2":2, "Element3":3}
for index, (key,value) in enumerate(dictionary.items()):
    print(index, key,value)

# Filter function
def odd(x):
    return not (x%2)==0
print(odd(3))
x=[1,2,3,4,5,6,7,8,9,10,11]
result = filter(odd,x)
for r in result:
    print(r)

# Map Function
def square(x):
    return x**2

x = [1,2,3,4,5]
squaredX = map(square,x)
for r in squaredX:
    print(r)

# Range Function
for i in range(0,5):
    print(i)

for i in range(10,1,-1):
    print(i)

listFromRange = list(range(0,9)) # to get a collection put it inside a list

# Slice Function
a = "test"
for letter in range(0, len(a)):
    print(a[letter])

print("Backwards")
for letter in range(0, len(a)):
    print(a[-(letter+1)])
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[0:4:2])
print(a[::-1])