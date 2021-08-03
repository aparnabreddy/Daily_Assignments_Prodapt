import re
textinput=input("enter a text:")
#val=re.search("^The",textinput)#^ it is used for checking the first word
#val=re.search("The$",textinput)#$ it is used for ends with the particular letter
# val=re.search("^The.*Hello$",textinput)
val=re.search("^The.Hello$",textinput)
if val:
    print("Accepted")
else:
    print("Rejected")
