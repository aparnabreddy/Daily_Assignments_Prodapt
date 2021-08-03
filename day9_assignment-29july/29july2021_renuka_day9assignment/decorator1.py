def hello(fn):
    def sayhello():
        print("hello")
        fn()
    return sayhello

@hello            # through decorator we can pass function as argument to another function
def sayhi():
    print("hi")
sayhi()