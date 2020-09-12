from enum import Enum

class MyClass:
    State = Enum("State", "Off Booting Running Shutdown")
    
    def __init__(self):
        self.myState = MyClass.State.Off
        
    def setState(self, state):
        if state in MyClass.State:
            self.myState = state
    
    def getState(self):
        return self.myState
    
mc = MyClass()
print(mc.getState())
mc.setState(MyClass.State.Running)
print(mc.getState())
print(mc.getState().name)