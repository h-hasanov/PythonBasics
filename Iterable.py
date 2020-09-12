class PowerOfTen:
    """ This class is an example of an iterable in Python """
    maxIterations = 10

    def __init__(self):
        self.counter = 0
    
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter<PowerOfTen.maxIterations:
            result = 10**self.counter
            self.counter+=1
            return result
        else:
            raise StopIteration
help(PowerOfTen)

it = iter(PowerOfTen())
print(next(it))

for x in PowerOfTen():
    print(x)

