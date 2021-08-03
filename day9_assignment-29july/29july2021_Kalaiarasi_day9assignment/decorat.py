# def add(a,b):
#     return a+b
# print(add(2,3))
# x=add
# print(x(2,3))


# class dec:
#    def __init__(self,a,b):
#        self.a=a
#        self.b=b
#        print("dec")
# obj1=dec
# obj1(1,2)

# def sum(a,b):
#     return a+b
# def diff(a,b):
#     return a-b
# def operation(op,x,y):
#     result=op(x,y)
#     return result
# print(operation(sum,10,5))
# print(operation(diff,10,5))


def hello(fn):
    def sayhello():
        print("hello")
        fn()
    return sayhello
@hello
def sayhi():
    print("hi")
sayhi()