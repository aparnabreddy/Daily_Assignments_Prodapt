employeedict={}
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
    print("3) salary")
    print("4) exit ")
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
        sal=int(input("Enter the Salary to check: "))
        salarylist=[i for i in employeedict.maps if int(i['salary'])>=sal]
        for i in salarylist:
            print(i)
            
    if option==4:
        break
#3)display all the employees who as salary grater than amount specified by user by using list comprehension

#2)prgram
'''menu driver 1)add student(nmae,rollno,adminno,marks of 5 subjects) use the oops concepts (inheritance)
             2) search students details using rollno 
               3)List students api with marks
               4)print all the students based on ranking (sum of marks)'''
                
