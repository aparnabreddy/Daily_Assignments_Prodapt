import re
#name
FirstName=input("Enter the Full Name:")
val=re.search("^(Mr\.|Mrs\.|Ms\.)[A-Za-z]{2,25}\s[A-Za-z]{2,25}",FirstName)
if val: print("Valid User Name") 
else: print("Invalid User Name") 

#mbl number
mblno=input("Enter the mblno.:")
val=re.search("^91[6-9]\d{9}$",mblno)
if val: print("Valid Mobile Number") 
else: print("Invalid Mobile Number") 

#Address
Address=input("Enter the Address:")
val=re.search("^[0-9a-zA-Z\s,-]+$",Address)
if val: print("Valid Address") 
else: print("Invalid Address")

#pincode
pincode=input("Enter the pincode:")
val=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode) 
if val: print("Valid Pincode Number") 
else: print("Invalid Pincode Number") 

#Email
email=input("Enter the Email:")
val=re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",email) 
if val: print("Valid Email Id") 
else: print("Invalid Email Id")