# def simple(a,b):
#     return a+b
# # print(simple(2,3))
# x=simple
# print(x(2,3))


# class decarator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("decarator is working")

# obj=decarator
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
        print("hello")
        fn()
    return sayhello

@hello
def sayhi():
    print("hi")

sayhi()


