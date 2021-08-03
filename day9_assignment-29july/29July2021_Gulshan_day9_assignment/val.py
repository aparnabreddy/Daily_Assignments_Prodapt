import re
name=input("enter the name: ")
mobile=input("enter the number: ")
pincode=input("enter the pincode: ")
address=input("enter the address: ")
emailId=input("enter the email id: ")
nam=re.search("^[a-zA-Z\s\.]*$",name)
if nam:
    print("Name is acccepted",name)
else:
    print("Name is incorrect",name)
val1=re.search("^[6-9]\d{9}$",mobile)
if val1:
    print("Mobile no is accepted",mobile)
else:
    print("Mobile no is incorrect",mobile)
val2=re.search("^[4]\d{5}$",pincode)
if val2:
    print("PIn code acccepted",pincode)
else:
    print("pincode is incorrect",pincode)
val3=re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailId)
if val3:
    print("email id accepted",emailId)
else:
    print("invalid email.id",emailId)
# print("your name is ",name)
# print("Your phone No. is ",mobile)
# print("Your pin code is ",pincode)
# print('your address is ',address)
# print('Your email ID is ',emailId)