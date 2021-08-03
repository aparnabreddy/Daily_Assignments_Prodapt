employeedict={}
from os import name
import re,collections,time
def getdatetime():
    time1=time.localtime()
    currentime=time.strftime("%Y-%m-%d %H:%M:%S ",time1)
    return currentime
def addEmployee():
    id=input("enter the id :")
    name=input("enter the name: ")
    designation=input("enter the Designation: ")
    salary=input("Enter the salary :")
    address=input("Enter the address : ")
    pincode=input("Enter the pincode : ")
    timedate1=getdatetime()
    dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode,'addedOn':timedate1}
    return dict1
def validate(dict1):
    valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
    valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
    valpincode=re.search("(^6)[0-9]{5}$",dict1["pincode"])
    if valname and valsalary and valpincode:
        return True
    else:
        return False

while(1):
    print("1)add emplyee")
    print("2) view employee")
    print("3) exit")
    option=int(input("Enter your option :"))
    if option==1:
        a=addEmployee()
        if validate(a):
            if len(employeedict)==0:
                employeedict=collections.ChainMap(a)
            else:
                employeedict=employeedict.new_child(a)
    if option==2:
        print(employeedict.maps)
    if option==3:
        break
#print(employeedict.maps)
