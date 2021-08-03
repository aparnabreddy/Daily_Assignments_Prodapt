import re
name=input("enter your name :")
validation1=re.compile(r'([a-zA-Z])\D*([a-zA-Z])$')
res=validation1.search(name)

if res:
    print("accepted")
else:
    print("rejected")