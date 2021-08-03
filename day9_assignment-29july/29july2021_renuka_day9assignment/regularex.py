#regular expressions are used for validation purpose.sequence of characters which are used to find the sequence of other characters
import re
textinput=input("enter a text")
val=re.search("^The",textinput)#starts with
val1=re.search(".hello$",textinput)#ends with
print(val1)