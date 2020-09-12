listWithDuplicates = [1,2,1,2,3,4,1,2,3,4,5,6,7,1,2,3]
setWithoutDuplicates = {x for x in listWithDuplicates}
print(setWithoutDuplicates)

squaredSet = {x*x  for x in listWithDuplicates}
print(squaredSet)

unimportantWords = ["the", "and", "i", "or", "this", "of", "to", "if"]
sentence = "This is a test of the emergency broadcast which tests to see if the world has broken down"
wordList = sentence.split(" ")
importantWords = {x.lower() for x in wordList if x not in unimportantWords}
print(importantWords)