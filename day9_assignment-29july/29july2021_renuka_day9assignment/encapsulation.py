class MobilePhone:
    def __init__(self):
        self.__price=2000
    def sellingprice(self):
        print(self.__price)
    def offerprice(self,discount):
        self.__price=self.__price-discount
mobile=MobilePhone()
mobile.sellingprice()
mobile.__price=500
mobile.sellingprice()
mobile.offerprice(500)
mobile.sellingprice()