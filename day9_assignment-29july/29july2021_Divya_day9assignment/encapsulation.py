class Mobile_phone:
    def __init__(self):
        self.__price = 2000
        self.x = 500
    def selling_price(self):
        print(self.__price)
        print("x = ",self.x)
    def offer_price(self,discount):
        self.__price = self.__price - discount
mobile = Mobile_phone()
mobile.selling_price()
mobile.__price=500
mobile.offer_price(500)
mobile.selling_price()
mobile.x = 1000

