import re
mobile=input("enter a mobile number")

validation=re.search("^[6-9]\d{9}$",mobile)#[0-9]ord{9}

if validation:
    print("accepted")
else:
    print("rejected")
#collect values from user i.e name,mono,add,pin,emailid write the validations for all the details
name=input("enter your name")
validation1=re.compile(r'([a-zA-Z])\D*([a-zA-Z])$')
res=validation1.search(name)

if res:
    print("accepted")
else:
    print("rejected")
emailid=input("enter your email id")
validation3=re.search("^[a-zA-Z]+[\._]?[a-zA-Z]+[@]\w+[.]\w{2,3}$",emailid)
if validation3:
    print("accepted")
else:
    print("rejected")
