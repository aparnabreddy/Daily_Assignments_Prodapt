import re
mobile=input("enter a mobile number")

validation=re.search("^[6-9]\d{9}$",mobile)#[0-9]ord{9}

if validation:
    print("accepted")
else:
    print("rejected")