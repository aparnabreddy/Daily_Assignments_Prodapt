import collections
import re
Emp_dict={}

# -----Function to add employee-----
def addEmployee():
    Emp_name=(input("Enter Employee Name: "))
    Emp_id=(input("Enter Employee ID: "))
    Designation=(input("Enter the Employee Designation: "))
    Salary=(input("Enter Employee salary: "))
    Address=(input("Enter Employee address: "))
    Mob_no=(input("Enter Employee mobile number: "))
    Pincode=(input("Enter the pincode: "))
    dict1={"Emp_name":Emp_name,"Emp_id":Emp_id,"Designation":Designation,"Salary":Salary,"Address":Address,"Mob_no":Mob_no,"Pincode":Pincode}
    return dict1

#-------Validation function------
def validation(dict1):
    valemp_name=re.search("[A-Z]{1}[^A-Z]{0,30}$",dict1["Emp_name"])
    valsalary=re.search("[0-9]{0,8}$",dict1["Salary"])
    valmob_no=re.search("[6-9]{1}[0-9]{9}$",dict1["Mob_no"])
    if valemp_name and valsalary and valmob_no:
        return True
    else:
        return False


# -----Menu------
while(True):
    print("1.Add Employee")
    print("2.View Employee")
    print("3.Salary check")
    print("4.Exit")
    choice=(int(input("Enter your response: ")))
    if choice == 1:
        addEmployee=addEmployee()
        if validation(addEmployee):
            if len(Emp_dict)==0:
                Emp_dict=collections.ChainMap(addEmployee)
            else:
                Emp_dict=Emp_dict.new_child(addEmployee)

    if choice == 2:
        print("Employee details")
        print(Emp_dict.maps)
    if choice==3:
        Sal=int(input("Enter the salary to check: "))
        Salarylist=[i for i in Emp_dict.maps if int(i['Salary'])>Sal]
        for i in Salarylist:
            print(i)
    if choice==4:
        print("Exit from the menu")
        break