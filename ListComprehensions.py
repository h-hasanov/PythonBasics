squares = [n**2 for n in range(0,10)]
print(squares)

listOfNumbers = range(0,11)
listOfOdds = [o*o for o in listOfNumbers if o%2!=0]
print(listOfOdds)

randomText = "Lets make a list out of a sentence"
lettersFromRandomText = [c.upper() for c in randomText]
print(lettersFromRandomText)

multipleSources = [x+y+z for x in range(1,5) for y in range(5,10) for z in range(10,15)]
print(multipleSources)

print(["zero" if v == 0 else "odd" if v%2!=0 else "even" for v in range(0,10)])