import numpy

myList = [1,2,3,4,5,6]
myNumpyArray = numpy.array(myList)
print(myNumpyArray)
print(myNumpyArray.shape)

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

matrix = numpy.array([row1, row2, row3])
print(matrix)
print(matrix.shape)

zeroMatrix = numpy.zeros((3,3))
print(zeroMatrix)
onesMatrix = numpy.ones((2,3))
print(onesMatrix)
anyNumbersMatrix = numpy.full((2,3),1234)
print(anyNumbersMatrix)

subArray = matrix[0:3, 1]
print(subArray.shape)
print(subArray)

fiveColumns = numpy.array(numpy.arange(0, 5))
print(fiveColumns)

floatMatrix = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.7],
                           [1.5, 2.5, 3.5]], dtype = numpy.float)
print(floatMatrix.shape)
print(floatMatrix)
print(floatMatrix.dtype)
print(floatMatrix*2)

irow1 = [1,2,3]
irow2 = [4,5,6]
irow3 = [7,8,9]
integerMatrix = numpy.array([irow1, irow2, irow3], dtype=numpy.int)

frow1 = [11.0, 12.0, 13.0]
frow2 = [14.0, 15.0, 16.0]
frow3 = [17.0, 18.0, 19.0]
floatMatrix = numpy.array([frow1, frow2, frow3], dtype=numpy.float)

print(integerMatrix+floatMatrix)

cmp1 = [(1+2j), (2+3j), (3+4j)]
cmp2 = [(4+5j), (5+6j), (6+7j)]

complex1 = numpy.array(cmp1)
complex2 = numpy.array(cmp2)
print(complex1+complex2)

print(numpy.round(floatMatrix, 2))
print(numpy.floor(floatMatrix))

print(floatMatrix.sum(axis = 0))
print(floatMatrix.sum(axis = 1))
print(floatMatrix.sum())