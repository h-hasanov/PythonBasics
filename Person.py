class Person:
    def __init__(self):
        self.name = ""
        self.age = -1
        
    def setAge(self, age):
        self.age = age
        return self

    def getAge(self):
        return self.age
    
    def setName(self, name):
        self.name = name
        return self
    
    def getName(self):
        return self.name
    