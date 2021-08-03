import re

name = input("enter a name: ")
num = input("enter a phone number: ")
pin_code = input("enter a pin code: ")
e_id = str(input("enter a email id: "))
#address = input("enter the address: ")

val = re.search("^D.*a",name)
val1 = re.search("^\+91?[6-9]\d{9}$",num)
val2 = re.search("^6\d{5}$",pin_code)
val3 = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if val:
    print("1.the name is acceptable:",name)
else:
    print("enter a correct name")
if val1:
    print("2.Number is  acceptable: ",num)
else:
    print("The number is incorrect")
if val2:
    print("3.Pincode  is  acceptable: ",pin_code)
else:
    print("the pin code is incorrect")
if val3:
    print("4.valid mail address: ",e_id)
else:
    print("invalid email address")

# print(val)
# print(val1)
# print(val2)
# print(val3)

