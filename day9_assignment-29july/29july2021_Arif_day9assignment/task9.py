import re
name=input("enter the name:")
mobile=input("enter the mobile:")
pin=input("enter the pincode:")
email=input("enter the email address:")
validation=re.search("^[6-9]\d{9}$",mobile)
if validation:
      print("number accepted")
      print(mobile)
else:
    print("mobile number rejected")

validation1=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pin) 
if validation1:
     print("pincode accepted")
     print(pin)
else:
   print(" pincode rejected")

validation2=re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",email)
if validation2:
      print("emailaccepted")
      print(email)
else:
    print(" email rejected")