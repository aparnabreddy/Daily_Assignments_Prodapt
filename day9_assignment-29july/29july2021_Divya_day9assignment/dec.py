# def add(a,b):
#     return a+b 
# x =add
# print(x(3,2))

# class decorators:
#     def __init__(self,a,b):
#         self.a= a
#         self.b= b
#         print("dec is working")
# obj = decorators
# obj(4,5)

# def sum(a,b):
#     return a+b
# def difference(a,b):
#     return a-b
# def st(a,b):
#     return "the string is '{}','{}' " .format(a,b)
# def operation(op,x,y):
#     result =op(x,y)
#     return result
# print(operation(sum,10,5))
# print(operation(difference,6,4))
# print(operation(st,"divya","da"))

def hello(fn):
    def sayhello():
        print("hello")
        fn()
    return sayhello
@hello
def sayhi():
    print("hi")
sayhi()

