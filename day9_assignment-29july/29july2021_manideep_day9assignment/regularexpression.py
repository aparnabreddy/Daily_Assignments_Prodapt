import re
name=input("enter a name:")
val1=re.search("^[a-zA-Z\s\.]*$",name)
if val1:
    print("accepted")
else:
    print("rejected")
mobile=input("mobile number:")
validation=re.search("^[6-9]\d{9}$",mobile)
if validation:
    print("Accepted")
else:
    print("Rejected")

email=input("enter email:")
em=re.search("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)
if em:
    print("accepted")
else:
    print("rejected")
pincode=input("enter pincode:")
pi=re.search("^[1-9]\d{5}$",pincode)
# val1=re.search("^the",textinput)
# val=re.search("hello$",textinput)

if pi:
    print("accepted")
else:
    print("rejected")

print(name)
print(mobile)
print(email)
print(pincode)