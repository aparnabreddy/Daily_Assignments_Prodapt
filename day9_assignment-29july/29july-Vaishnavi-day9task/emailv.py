import re
emailid=input("enter your email id :")
validation3=re.search("^[a-zA-Z]+[\._]?[a-zA-Z]+[@]\w+[.]\w{2,3}$",emailid)
if validation3:
    print("accepted")
else:
    print("rejected")
