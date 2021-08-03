import re
mobile=input("Enter a mobile number:")
validation=re.search("^[6-9]\d{9}$",mobile)
if validation:
    print("Accepted")
else:
    print("Rejected")