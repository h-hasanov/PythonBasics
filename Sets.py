# Like dictionaries, sets are unordered collections of data in Python.
# It contains set of values which must be unique

set1 = {1,2,3,4,3,2,1}
print(set1)

set2 = set([1,2,3,4,3,2,1])
print(set2)

# Add/Remove
set1.add(99)
set1.discard(2)
set1.remove(4)
print(set1)

# Operations
s1 = set([1,2,3,4,5])
s2 = set([6,7,8,9,10])
print(s1|s2) # s1 or s2 (union)

s1 = set([1,2,3,4,5,6])
s2 = set([3,4,5,6,7,8])
print(s1&s2) # s1 and s2 (intersection)
print(s1-s2) # in s1 but not in s2

s1 = [1,2,3,4,5]
s2 = [2,3,4]
print(s1<=s2) # s1 is a superset of s2
print(s2 >= s1) # s2 is a subset of s1