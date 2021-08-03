stud_dict = dict()

def addStudent():
    roll_no = int(input("Enter the roll number: "))
    name = input("Enter the name of the student: ")
    Adminno= int( input("Enter the Admin number: "))
    m1 = int (input("Enter the marks in 1st subject: "))
    m2 = int (input("Enter the marks in 2nd subject: "))
    m3 = int (input("Enter the marks in 3nd subject: "))
    m4 = int (input("Enter the marks in 4nd subject: "))
    m5 = int (input("Enter the marks in 5nd subject: "))
    marks=(m1+m2+m3+m4+m5)
    average=marks/5
    print(end="Average Mark = ")
    print(average)
    stud_dict[roll_no] = name,Adminno, average


while(1):
    print("1. Add Student")
    print("2. Search Student Based On Roll Number")
    print("3. Studentapi")
    print("4. Exit")
    option=int(input("Enter your option :"))
    if option==1:
        a=addStudent()
        pass
    if option==2:
        srn = int(input("Enter the roll number of the student whose details you'd like to view: "))
        if srn in stud_dict:
            print(stud_dict[srn])
        else:
            print("No such student.")
    print(stud_dict)
    if option==3:
        print()
    if option ==4:
        break
