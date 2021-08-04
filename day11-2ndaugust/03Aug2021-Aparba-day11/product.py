import datetime,time
import re
from datetime import date
productslist=[]
class ProductDetails:
    def addproductdetails(self, prod_name, prod_desc, prod_price,manufacturer,manufacturing_date,expiry_date):
        dict1={"prod_name":prod_name,"prod_price":prod_price,"prod_desc":prod_desc,"manufacturer":manufacturer,"manufacturing_date":manufacturing_date,"expiry_date":expiry_date}
        productslist.append(dict1)

def validation(prod_name,prod_price):
    valname=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",prod_name)
    valprice=re.match("[0-9]{0,7}$",prod_price)
    if valname and valprice:
        return True
    else:
        return False
obj1=ProductDetails()
while(True):
    print("1.Add product")
    print("2.View all products")
    print("3.Search product using product name")
    print("4.List of products that expire today")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        prod_name=input("Enter name of the product: ")
        prod_desc=input("Enter product description: ")
        prod_price=input("Enter the price of product: ")
        manufacturer=input("Enter manufacturer name: ")
        manufacturing_date=input("Enter date of manufacturing: ")
        expiry_date=input("Enter expiry date DD-MM-YYYY: ")
        if validation(prod_name,prod_price):
            obj1.addproductdetails(prod_name, prod_desc, prod_price,manufacturer,manufacturing_date,expiry_date)
        else:
            print("Invalid product name and price")
            continue
        
    if choice==2:
        print(productslist)
    if choice==3:
        pname=input("Enter the product name to saearch: ")
        print(list(filter(lambda i:i["prod_name"]==pname,productslist)))
    if choice==4:
        current_time=time.localtime()
        today=time.strftime("%d-%m-%Y",current_time)
        expiryprodlist=(list(filter(lambda i:i["expiry_date"]==str(today),productslist)))    
        if len(expiryprodlist)>0:
            print(expiryprodlist)
        else:
            print("No products that expire today")  
    if choice==5:
        break