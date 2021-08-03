import re
num= input("Enter your phone no.: ")
val = re.search("^[6-9]\d{9}$",num)
if val:
    print('number accepted')
else:
    print("number rejected")