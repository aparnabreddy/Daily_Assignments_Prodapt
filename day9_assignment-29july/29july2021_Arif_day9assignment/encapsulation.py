class MobilePhone:
    def __init__(self):
        self.__price=2000
        self.x=500
    def sellingPrice(self):
        print(self.__price)
        print(self.x)

    def offerPrice(self,discount):
        self.__price=self.__price - discount

obje=MobilePhone()
obje.sellingPrice()
obje.offerPrice(1000)
obje.sellingPrice()
obje.x=60
obje.sellingPrice()

