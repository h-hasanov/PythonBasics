def hello(f):
    def wrapper(name):
        print("Hello ", end = '')
        f(name)
    return wrapper

@hello
def printName(name):
    print(name)

printName('fred')


def check(inputType):
    def checker(f):
        def checkedFunc(arg):
            if isinstance(arg, inputType):
                return f(arg)
            else:
                raise TypeError
        return checkedFunc
    return checker

@check(int)
def printInt(val):
    print(val)

printInt(100)


def test():
    def decorator(func):
        func.isTest = True # or setattr(func, 'is_test', True)
        return func
    return decorator

def isTest(test):
    if hasattr(test, 'isTest'):
        return True
    return False

@test()
def testAllTheThings():
    print("This is a test")

def notTestFunction():
    print("This is not a test function")
    
print("testAllTheThings is a test = {0}".format(isTest(testAllTheThings)))
print("notTestFunction is a test = {0}".format(isTest(notTestFunction)))

import time

def timer(func):
    def wrapper():
        t1 = time.time()
        res = func()
        t2 = time.time()
        wrapper.elapsedTime = t2-t1
        return res
    return wrapper

@timer
def aLongFunction():
    time.sleep(2)
    return 3

f = aLongFunction
print(f())
print(f.elapsedTime)