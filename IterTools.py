from itertools import count, cycle, repeat, groupby

for idx, val in enumerate(count(10)):
    if idx > 5:
        break
    print(val)
    
notes = ["do", "ri", "mi", "fa", "sol"]
for idx, n in enumerate(cycle(notes)):
    print(n)
    if idx > 8:
        break
    
for ans in repeat("yes", 3):
    print(ans)
    
list = [1, 2, 1, 3, 1, 4, 2, 3, 4]

for key, group in groupby(sorted(list), lambda x:x):
    print("Group: " + str(key))
    for element in group:
        print(' ' + str(element))
        
darray = [
    {
        "name": "matt",
        "city": "new york",
        "state": "NY"
    },
    {
        "name": "fred",
        "city": "albany",
        "state": "NY"
    },
    {
        "name": "irving",
        "city": "atlanta",
        "state": "GA"
    },
    {
        "name": "tony",
        "city": "duluth",
        "state": "MN"
    }
]

for key, group in groupby(darray, lambda x: x['state']):
    print("Group: " + str(key))
    for element in group:
        print(' ' + str(element))