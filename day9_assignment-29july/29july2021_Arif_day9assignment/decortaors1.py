def Hello(fn):
    def sayHello():
        print("helllo")
        fn()
    return sayHello
@Hello
def sayHi():
    print("hi")        
sayHi()