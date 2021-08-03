# "^hello"     matches any string that start with Hello
# "hello$"     matches any string that end with hello
# "^hello$"    matches any string that start and  with hello
# "hello"      matches any string that contains hello
# "hello*"     matches a particular string any string that contains 0 or more than o's.
# "hello?"       there might be a single O(letter o) or not.

# Example
# import re
# var="abcbcbcbc"
# # # regex=re.search("a?b+$",var)
# # # regex=re.match("ab{2,8}",var)
# # # regex=re.match("a(bc)*",var)
# regex=re.match("^a(bc){2,4}$",var)
# # regex=re.match("a(bc){2,4}",var)
# # # regex="xb"
# # # v=re.search("hello*",var)
# # # v=re.search("hello+",var)
# # # v1=re.search("hello?",var)
# print(regex)

# {}      to specify range
# ()      for group 

# import re
# var="hii"
# regex=re.match("(hello|hii)+x",var)
# print(regex)

# |(or dot operator)    

import re
var="9926334635"
# re2=re.match("a.[0-9]",var)
# re2=re.match("[a-zA-Z]*[0-9]{3}",var)
# re2=re.match("^[A-Z]{5}$",var)
# re2=re.match("^[a-zA-Z]",var)
# re2=re.match("^[0-9]{2}%$",var)
re2=re.match("^(\+91)?[0]?(91)?[6-9]\d{9}$",var)
print(re2)
