import re
name=input("enter the name:")
print(name)
mobile=input("enter the number:")
val1=re.search("^[6-9]\d{9}$",mobile)
if val1:
    print(mobile)
else:
    print("phone no is incorrect")
pincode=input("enter the pincode:")
val2=re.search("^[5]\d{6}$",pincode)
if val2:
    print(pincode)
else:
    print("pincode is incorrect")
address=input("enter the address:")
print(address)
emailId=input("enter the email id:")
val3=re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailId)
if val3:
    print(emailId)
else:
    print("invalid email.id")


    