import inspect
import sys

def loadModule(name):
    module = __import__(name)
    return module

def getClasses(module):
    classNames = []
    for name in dir(module):
        obj = getattr(module, name)
        if inspect.isclass(obj):
            classNames.append(name)
    return classNames

def describeFunc(obj):
    sig = inspect.signature(obj)
    print(" Arguments: ")
    for s in sig.parameters:
        print(' {0}'.format(s))
        
def describeClasses(fileName):
    module = fileName.replace('.py','').replace('/', '.')
    mod = loadModule(module)
    entries = getClasses(mod)
    obj_dict = {}
    
    for e in entries:
        obj = getattr(mod, e)
        if inspect.isclass(obj):
            print("Class: {0}".format(e))
            try:
                ins = obj()
                methods = inspect.getmembers(ins, predicate = inspect.ismethod)
                for mn, mv in methods:
                    print(" Method: {0}".format(mn))
                    describeFunc(mv)
                    print(" Attributes:")
                    for name in ins.__dict__:
                        print(' ' + name)
            except Exception(e):
                print(e)
            obj_dict[e] = ins
    return obj_dict
                
d = describeClasses('Person.py')
person = d['Person']
getAge = getattr(person, "getAge")
age = getAge()
print(age)

setAge = getattr(person, "setAge")
setAge(29)
age = getAge()
print(age)

def aFunctionsWithParameters(a,b,c,d):
    x = a+b+c
    y = b+c+d
    z = c+d+a
    print(x,y,z)

funcPtr = getattr(sys.modules[__name__],'aFunctionsWithParameters')
funcPtr(1,2,3,4)