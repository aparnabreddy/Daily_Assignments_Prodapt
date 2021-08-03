class Phone:
    def __init__(self):
        self.__price=2000
        self.x=500
        
    def sellingprice(self):
        print(self.__price)
        print("x= ",self.x)

    def offerprice(self, discount):
        self.__price=self.__price-discount

pno=Phone()
pno.sellingprice()
pno.__price=500
pno.sellingprice()
pno.offerprice(500)
pno.sellingprice()
pno.x=1000
pno.sellingprice()