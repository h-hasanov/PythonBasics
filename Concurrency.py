import time
from threading import Thread

def printNames(names):
    for name in names:
        print(name)
        time.sleep(1)

def printReverseNames(names):
    for name in names:
        print(name[::-1])
        time.sleep(1)
        
names = ["Anita", "Barry", "Christian", "Daniel", "Edward", "Fred", "George"]

t1 = time.time()
thread1 = Thread(target=printNames, args=(names,))
thread2 = Thread(target=printReverseNames, args=(names,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
t2 = time.time()
print("Time: {0}".format(t2-t1))