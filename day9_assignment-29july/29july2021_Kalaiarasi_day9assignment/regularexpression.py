import re
textinput=input("enter a text:")
#val=re.search("^The",textinput)
#val=re.search(".*Hello$",textinput)
val=re.search("^The.*Hello$",textinput)
if val:
    print("Accepted")
else:
    print("Rejected")