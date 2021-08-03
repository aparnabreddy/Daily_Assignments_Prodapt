def Hello(fn):
    def sayhello():
        print("Hello")
        fn()
    return sayhello

@Hello
def sayhi():
    print("hi")

sayhi()