from random import randint
from collections import Counter

my_list = [] # Empty List
my_list = [1,2,3] # Homogeneous Array

my_list = [1,2.5,"Hello World"] # NonHomogeneous Array
print(my_list)

len(my_list) # length of list
print(len(my_list))

print(2.5 in my_list)

my_list = [1,2,3]
my_list_2 = ["fred"]
print(my_list+my_list_2)

# Object removal
my_list = [1,2,3,3,4,3]
my_list.remove(3) # removes only the first found instance.
# Remove removes elements by value
print(my_list)

del my_list[0] # del removes by index
print(my_list)


#Add/Insert
my_list.append(1000)
my_list.insert(0,5)
print(my_list)
my_list[0]=999
print(my_list)

# Unpacking
def unpackList(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)

# The unpacking operator is *
l = [1,2,3]
unpackList(*l)

list1 = [randint(0,100) for x in range(0,10)]
def funcToFilter(x):
    if x>10 and x<50:
        return True
    return False
filteredList = list(filter(funcToFilter, list1))
print(filteredList)

arrayOfIntegers = [x for x in range(0,10)]
print(arrayOfIntegers)
reversedArrayOfIntegers = arrayOfIntegers[::-1]
print(reversedArrayOfIntegers)
evenNumbers = arrayOfIntegers[2::2]
print(evenNumbers)

def mostCommonCounter(listInput):
    data = Counter(listInput)
    return data.most_common(1)[0][0]

list1 = [1,2,3,2,3,2]
print(mostCommonCounter(list1))