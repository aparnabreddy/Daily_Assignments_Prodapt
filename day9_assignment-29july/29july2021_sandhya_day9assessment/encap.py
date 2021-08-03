class Encap:
    __a=10
    def display(self):
        print("welcome")
        print(self.__a)
obj=Encap()
#print(object.__a) #here we are accesing private variable in outside the class so it will show an error
obj.display()