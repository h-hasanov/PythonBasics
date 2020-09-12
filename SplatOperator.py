def sumUp(total, *args, **kwargs):
    for x in args:
        total+=x
    
    for ik in kwargs.items():
        total+=ik[1]
    
    return total
print(sumUp(100,2,3,4,5,6, value=1, value2=2))
print(sumUp(100,value=1, value2=2))
print(sumUp(100,2,3,4,5,6))

