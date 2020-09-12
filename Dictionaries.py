dictionary = {"Key1": "value1", 1024:"Second element has non-string key", "Key3":"ddd"}
print(dictionary)
# The only requirement for a key in a dictionary is that the key must be of an
# immutable type, such as string, numeric or boolean

print(dictionary[1024]) # print element for a given key

print (3 in dictionary) # check whether a key is in list of keys

for key in dictionary:
    print("Key:{0}, value:{1}".format(key, dictionary[key]))

print(len(dictionary)) # number of keys in dictionary

# Add/Insert items
dictionary["newItem"] = "this is a new Item" # insert a key-value pair into a dictionary 
dictionary["Key1"] = "this is value replacement" # replace a value by key
print(dictionary)

# Remove Items
del dictionary["Key1"] #remove by key using del operator
dictionary.pop("newItem") # remove from dictionary using pop function
print (dictionary)

# Nested Dictionary
nestedDictionary = {
    "Item1":{
        "Name":"A",
        "Age":1
    },
    "Item2":{
        "Name":"B",
        "Age":2
    }
}

item3Dictionary = {"Name":"C", "Age":3}
nestedDictionary["Item3"] = item3Dictionary
print(nestedDictionary)