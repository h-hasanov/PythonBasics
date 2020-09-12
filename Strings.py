listOfWords = [1.0, "this is a test", 2, "c", "hello world"]
s = " ".join([str(x) for x in listOfWords])
print(s)

stringToSearch = "This is a test of the emergency broadcast system. This is not an error"
print("String contains error {0}".format("error" in stringToSearch))
print("Position {0}".format(stringToSearch.find("error")))
print("String contains error {0}".format("Error" in stringToSearch))