import time
import json
import datetime
import pickle
from random import randint

f = open("test.txt","w")
for i in range(1,5):
    f.write("{0}: This is a test number {1}\n".format(time.time(),i))
f.close()

warningLevels = ["info", "warning", "error", "critical error"]
with open('test2.txt', 'a') as f:
    which = randint(0, len(warningLevels)-1)
    f.write('{0}: This is a {1} at {2}\n'.
    format(warningLevels[which], warningLevels[which], time.time()))

# Reading Fixed Length Files

with open('FixedLengthFile.txt') as fixed:
    done = False
    while not done:
        lineCode = fixed.read(3)
        if len(lineCode) != 3:
            done = True
            continue
        description = fixed.read(18)
        alpha_code = fixed.read(5)
        last_code = fixed.read(5)
        spacing = fixed.read(1)

        print(lineCode)
        print(description)
        print(alpha_code)
        print(last_code)
        print(spacing)

def read_block(fileObj, size):
    while True:
        data = fileObj.read(size)
        if not data:
            break
        yield data

fields = [
    ('line_code', 3),
    ('description', 18),
    ('alpha_code', 5),
    ('last_code', 5),
    ('spacer', 1)
    ]

# with open('FixedLengthFile.txt') as fixed:
#     done = False
#     while not done:
#         for field in fields:
#             block = next(read_block(fixed, field[1]))
#             if len(block) != field[1]:
#                 done = True
#                 break
#             print("Read block for {0}={1}".format(field[0], block))

# Reading files line by line
with open('text_lines.txt') as lines:
    done = False
    while not done:
        newLine = lines.readline()
        if not len(newLine):
            done = True
        else:
            newLine = newLine[0:len(newLine)-1]
            print('['+newLine+']')

with open('text_lines.txt') as allLines:
    for line in allLines:
        line = line[0:len(line)-1]
        print(line)

# Tail File:
numberOfLines = 5
fileName = 'FileIO.py'

with open(fileName,'r') as f:
    lines = f.readlines()
    for i in lines[len(lines)-numberOfLines:len(lines)-1]:
        print(i[0:len(i)-1])

# Dealing with Binary Files
with open('myBinary.b', 'wb') as binary:
    text = 'Hello world!'
    l = len(text)
    byteArray = l.to_bytes(4, byteorder = "big", signed = True)
    binary.write(byteArray)
    binary.write(text.encode('utf-8'))

with open('myBinary.b', 'rb') as binary2:
    data = binary2.read(4)
    l = int.from_bytes(data, byteorder="big", signed = True)
    print("length of string {0}".format(l))
    data = binary2.read(l)
    text = data.decode('utf-8')
    print(text)

# Dealing With JSON files
print("# Dealing With JSON files")
with open('testJson.json') as json_file:
    json_data = json_file.read()
    parsedData = json.loads(json_data)
    print(parsedData['name'])
    print(parsedData['dict']['value1'])

data = {
    'value1': 1,
    'value2': 2,
    'a_dict_of_values':{
        'd1': "hello",
        'd2': "world"
    },
    'value3': 1.234
}

with open('data.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# Serializing Objets with JSON
print("Serializing Objets with JSON")

class Person:
    def __init__(self, first, last, birthDate):
        self.firstName = first
        self.lastName = last
        self.birthDate = birthDate

def PersonEncoder(p):
    if isinstance(p, Person):
        output = {
            "first_name": p.firstName,
            "lastName": p.lastName,
            "birthDate": p.birthDate.strftime("%d %b %y")
        }
        return output
    else:
        type_name = p.__class__.__name__
        raise TypeError("Unexpected type {0}".format(type_name))

p = Person('Matt', "Telles", datetime.datetime(1991,1,6))
print(json.dumps(p, default=PersonEncoder))

class PersonEncoderClass(json.JSONEncoder):
    def default(self, obj):
        return PersonEncoder(obj)
print(json.dumps(p, cls=PersonEncoderClass))

lines = [
    'When in the cource of human events',
    'It becomes necessary for one people',
    'to dissolve the political bands which have connected them with another',
    'and to assume among the powers of the earth, the separate and equal station',
    "to which the Laws of Nature and Nature's God entitle them"
    ]

with open('thomas_jefferson.txt', 'w') as outLines:
    for line in lines:
        outLines.writelines(line+"\n")

data = [
    {
        'name': 'matt',
        'grade': 98.6,
        'days_missed': 4
    },
    {
        'name': 'teressa',
        'grade': 99.9,
        'days_missed': 0
    },
    {
        'name': 'sarah',
        'grade': 99,
        'days_missed': 12
    },
    {
        'name': 'rachel',
        'grade': 92,
        'days_missed': 4
    },
    {
        'name': 'jenny',
        'grade': 89,
        'days_missed': 0
    },
]
for d in data:
    print("%-10s %5.2f %3d" % (d['name'], d['grade'], d['days_missed']))

with open('formatted_data.txt','w') as formatted_output:
    for d in data:
        formatted_output.writelines("%-10s %5.2f %3d" % (d['name'], d['grade'], d['days_missed'])+"\n")


p = Person('Matt', "telles", datetime.datetime(1991,1,6))
with open('person.pickle', 'wb') as pickleFile:
    pickle.dump(p, pickleFile)

with open('person.pickle', 'rb') as pickleReader:
    p2 = pickle.load(pickleReader)
    print(p2.firstName, p2.lastName, p2.birthDate)