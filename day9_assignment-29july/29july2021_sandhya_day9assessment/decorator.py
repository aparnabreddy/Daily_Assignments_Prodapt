def sum(a,b):
    return a+b
def difference(a,b):
    return a-b
def operation(op,x,y):
    result=op(x,y)
    return result
print(operation(sum,10,5))
print(operation(difference,10,5))

