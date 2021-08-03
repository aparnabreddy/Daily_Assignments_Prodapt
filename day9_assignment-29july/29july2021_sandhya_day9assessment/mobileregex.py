import re
mobile=input("enter a mobile number:")
#validation=re.search("^[6-9]\d{9}$",mobile)
validation=re.search("^[6-9]\d{9}$",mobile)
if validation:
    print("accepted")
else:
    print("rejected")