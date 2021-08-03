import re 
text = input('enter the input ')
val = re.search("^hello .*The" ,text)
if val:
    print('Accepted')
else:
    print("Rejected")
