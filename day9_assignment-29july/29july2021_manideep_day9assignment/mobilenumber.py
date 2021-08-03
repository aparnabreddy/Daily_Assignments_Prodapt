import re
mobile=input("enter a mobile:")
validation=re.search("^[6-9]\d{9}$",mobile)
if validation:
    print("Accepted")
else:
    print("Rejected")

