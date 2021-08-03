class mobilephone:
    def __init__(self):
        self.__price=2000
        self.x=500
    def sellingprice(self):
        print(self.__price)
        print("x=",self.x)

    def offerprice(self,discount):
        self.__price=self.__price-discount

mobile=mobilephone()
mobile.sellingprice()
mobile.__price=500
mobile.sellingprice()
mobile.offerprice(500)
mobile.sellingprice()
mobile.x=1000
mobile.sellingprice()