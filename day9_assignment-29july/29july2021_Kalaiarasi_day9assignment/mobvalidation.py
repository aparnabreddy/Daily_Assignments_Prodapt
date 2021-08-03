import re
mobile=input("enter a mob num:")
val=re.search("^[6-9]\d{9}$",mobile)
if val:
    print("Accepted")
else:
    print("Rejected")