studentdict={}
from os import name
import re,collections,time
def getdatetime():
    time1=time.localtime()
    current_time=time.strftime("%Y-%m-%d %H:%M:%S ",time1)
    return current_time
def addstudent():
    Rollno=input("Enter the roll no. :")
    name = input("Enter the name: ")
    admino=input("Enter the admino. :")
    Maths=input("Enter the marks pf Maths :")
    Physics=input("Enter the marks of Physics :")
    Chemistry=input("Enter the marks of Chemistry :")
    English=input("Enter the marks of English :")
    datetime=getdatetime()
    dict1={"Rollno":Rollno,"name":name,"admino":admino,"Maths":Maths,"Physics":Physics,"chemistry":Chemistry,"English":English,"addedon":datetime}
    return dict1
def validate(dict1):
    valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
    if valname:
        return True
    else:
        return False
while(1):
    print("1.add student")
    print("2.view student")
    print("3.exit")
    option=int(input("Enter you option :"))
    if option==1:
        a=addstudent()
        if validate(a):
            # dict1=validate(a)
            if len(studentdict)==0:
                studentdict=collections.ChainMap(a)
            else:
                studentdict=studentdict.new_child(a)
    if option==2:
        print(studentdict.maps)
    if option==3:
        break
