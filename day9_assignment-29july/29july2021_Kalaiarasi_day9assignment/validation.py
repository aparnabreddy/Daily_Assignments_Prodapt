import re
email=input("enter a email:")
pincode=input("enter a pincode:")
name=input("enter a name:")
mobile=input("enter a mob num:")
print("\n")

#email validation
val=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",email)
if val:
    print(email)
else:
    print("invalid email")

#pincode validation
val=re.search("^[6]{1}[0-6]{1}\d{4}$",pincode)
if val:
    print(pincode)
else:
    print("invalid pincode")

#name validation
val=re.search("^[A-Za-z]{2,25}\s[A-Za-z]{2,25}",name)
if val:
    print(name)
else:
    print("invalid")

#mobile number validation
val=re.search("^[6-9]\d{9}$",mobile)
if val:
    print(mobile)
else:
    print("invalid mobile number")

