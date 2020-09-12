import time

class Meta(type):
    def __call__(self, *args, **kwargs):
        obj = object.__new__(self, args, kwargs)
        obj.createdAt = time.localtime()
        obj.__init__()
        return obj

class MySubCLass(metaclass = Meta):
    def __init__(self):
        self.__name__ = "Hello"
        
for i in range(0,4):
    msc = MySubCLass()
    t = msc.createdAt
    s = time.strftime("%Y-%m-%d %H:%M:%S", t)
    print("The object was created at {0}".format(s))
    time.sleep(2)