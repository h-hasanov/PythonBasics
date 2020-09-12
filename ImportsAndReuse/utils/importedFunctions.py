def doubleMe(x):
    return 2*x

def tripleMe(x):
    return 3*x

def reverseNumber(n):
    s = str(n)
    s = s[::-1]
    return int(s)

class Foo:
    def __init__(self):
        self.var = 100
    
    def SomeRandomFunction(self, x):
        return doubleMe(x)