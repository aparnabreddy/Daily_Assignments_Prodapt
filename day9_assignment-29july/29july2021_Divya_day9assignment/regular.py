import re

txt =  input("enter a text: ")
# if txt[0]= "the":
#val = re.search("^the",txt)
#val1 =re.search("india$",txt)
val1 = re.search("^The.*hello",txt)
if val1 :
    print("accepted")
else:
    print("rejected")
# print(val)
print(val1)
