class Mobilephone:
    def __init__ (self):
        self.__price=2000  #private variable
        self.x=500 #public variable

    def sellingprice(self):
        print(self.__price)
        print("x = ",self.x)
    
    def offerprice(self,discount):
        self.__price=self.__price-discount
mob=Mobilephone()
mob.sellingprice()
mob.__price=500
mob.sellingprice()
mob.offerprice(500)
mob.sellingprice()
mob.x=1000
mob.sellingprice()