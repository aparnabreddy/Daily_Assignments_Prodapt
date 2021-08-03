# def add(a,b):
#     return a+b
# x=add
# print(x(2,3))


# class decorator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("decorator is working")

# obj = decorator
# obj(3,4)

# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def operation(op,x,y):
#     result=op(x,y)
#     return result
# print(operation(sum,10,20))
# print(operation(sub,10,5))

def hello(fn):
    def sayhello():
        print('hello')
        fn()
    return sayhello 
@hello
def sayhi():
    print('hi')
sayhi()