
# def add(a,b):
#     return a+b

# print(add(2,3))
# x=add
# print(x(2,3))

# class decorator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("decorator is working")

# obj=decorator
# obj(1,2)

# def sum(a,b):
#     return a+b
# def difference(a,b):
#     return a-b
# def operation(op,x,y):
#     result=op(x,y)
#     return result
# print(operation(sum,10,5))
# print(operation(difference,10,5))

def hello(fn):
    def sayhello():
        print("Hello")
        fn()
    return sayhello
@hello
def sayhi():
    print("Hii")
sayhi()