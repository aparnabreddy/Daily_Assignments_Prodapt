class mobile:
    def __init__(self):
        self.__price=2000

    def sellingprice(self):
        print(self.__price)

    def offerprice(self,discount):
        self.__price=self.__price-discount
mob=mobile()
mob.sellingprice()
mob.__price=500
mob.sellingprice()
