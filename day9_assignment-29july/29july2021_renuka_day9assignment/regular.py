import re
textinput=input("enter a text")
val=re.search("^the.*hello$",textinput)
if val:
    print("accepted")
else:
    print("rejected")