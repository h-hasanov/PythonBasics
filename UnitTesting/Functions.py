import math
import datetime

def divide(v1, v2):
    if v2 == 0:
        return 0
    return v1/v2

def isTodayLeapDay():
    m = datetime.datetime.today().month
    d = datetime.datetime.today().day
    if m==2 and d==29:
        return True
    return False

def doSomethingWithLeapDay():
    if isTodayLeapDay():
        print("Doing something with Leap day")
    else:
        print("Not doing anything with leap days")
        
def SumFunction(a,b,c):
    return a+b+c

def SumOnes():
    return SumFunction(1,1,1)