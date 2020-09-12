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
        
readOnlyP = ReadOnlyP(20)
print(readOnlyP.__doc__)
print(readOnlyP.printX.__doc__)