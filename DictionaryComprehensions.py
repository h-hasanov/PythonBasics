randomData = [[1,"Value"], [2, "Gamma"], [10, "Delta"]]
dict1 = {v[1]:v[0] for k,v in enumerate(randomData)}
print(dict1)

listOfWords = ["the", "cat", "is", "on", "the", "roof"]
dict2 = {k:v for k,v in enumerate(listOfWords)}
print(dict2)

dictOfOdds = {k:k for k in range(0,10) if k%2!=0}
print(dictOfOdds)

squareFunc = lambda x: x*x
squaredDict = {k:squareFunc(k) for k in range(0,10)}
print(squaredDict)