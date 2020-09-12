oddGenerator = (x for x in range(0,10) if x % 2 !=0)
print(next(oddGenerator))

for v in oddGenerator:
    print(v)

def anIntegerGenerator(maxIters):
    for i in range(0,maxIters):
        yield i

integerGenerator = anIntegerGenerator(9)
for v in integerGenerator:
    print(v)