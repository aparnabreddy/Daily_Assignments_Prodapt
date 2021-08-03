import re
textinput=input("Enter a text :")
val=re.search("^The",textinput)
if val:
    print("Accepted")
else:
    print("Rejected")
# print(val)