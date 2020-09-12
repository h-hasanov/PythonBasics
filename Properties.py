class P:
    def __init__(self, x):
        self.x = x
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, v):
        if v>0 and v<1000:
            self.__x = v
            
class ReadOnlyP:
    """
    The P1 Class shows how to implement read-only properties
    """
    def __init__(self, x):
        self.__x = x            

    @property
    def x(self):
        return self.__x
    
    def printX(self):
        """
        This method prints out the value of x.
        It has no arguments
        """
        print(self.__x)

p = P(5)
p.x = 10
print(p.x)
p.x = 2000
print(p.x)

readOnlyP = ReadOnlyP(20)
print(readOnlyP.x)
readOnlyP.x = 100
print(readOnlyP.x)