import re
Students_List=[]
class StudentDetails:
    def addstudentdetails(self, name, rollno,admin,physics,chemistry,biology,maths,kannada,english):
        totalmarks=physics+chemistry+biology+maths+kannada+english
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"physics":physics, "chemistrt":chemistry, "biology": biology,"maths":maths,"kannada":kannada,"english":english}
        Students_List.append(dict1)


 # -----validation function----
def validation(valname,valrollno,valadmin):
    valname=re.search("^[A-Za-z]",name)
    valrollno=re.search("^[0-9",rollno)
    valadmin=re.search("^[0-9]",admin)
    if valname and valrollno and valadmin:
        return True
    else:
         return False
obj1=StudentDetails()


# -----menu------
while(True):
    print("1.Add student")
    print("2.Display students aa API")
    print("3.Search student using rollno")
    print("4.Ranking")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter the Student name: ")
        rollno=input("Enter the student rollno: ")
        admin=input("Enter the admin no: ")
        physics=int(input("Enter physics marks: "))
        chemistry=int(input("Enter chemistry marks: "))
        biology=int(input("Enter biology marks: "))
        maths=int(input("Enter maths marks: "))
        kannada=int(input("Enter kannada marks: "))
        english=int(input("Enter english marks: "))
        if validation(name,rollno,admin):
            obj1.addstudentdetails(name, rollno,admin,physics,chemistry,biology,maths,kannada,english)
    if choice==2:
        print(Students_List)
    if choice==3:
        srollno=int(input("Enter the rollno to search : "))
        print(list(filter(lambda i:i["rollno"]==srollno,Students_List)))
    if choice==4:
        print(sorted(Students_List,key=lambda i:i['total'],reverse=True))
    if choice==5:
        break