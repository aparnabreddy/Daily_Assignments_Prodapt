import re
num = input("enter a number: ")
val = re.search("^\+91?[6-9]\d{9}$",num)

if val :
    print("Number accepted")
else:
    print("Number rejected ")