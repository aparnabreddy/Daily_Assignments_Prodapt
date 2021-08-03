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
    if average>=91 and average<=100:
        print("Your Rank is A1")
    elif average>=81 and average<91:
        print("Your Rank is A2")
    elif average>=71 and average<81:
        print("Your Rank is B1")
    elif average>=61 and average<71:
        print("Your Rank is B2")
    elif average>=51 and average<61:
        print("Your Rank is C1")
    elif average>=41 and average<51:
        print("Your Rank is C2")
    elif average>=33 and average<41:
        print("Your Rank is D")
    elif average>=21 and average<33:
        print("Your Rank is E1")
    elif average>=0 and average<21:
        print("Your Rank is E2")
    else:
        print("Invalid Input!")

while(1):
    print("1. Add Student")
    print("2. Search Student Based On Roll Number")
    print("3. Exit")
    option=int(input("Enter your option :"))
    if option==1:
        s=addStudent()
        print(stud_dict)
    if option==2:
        srn = int(input("Enter the roll number of the student whose details you'd like to view: "))
        if srn in stud_dict:
            print(stud_dict[srn])
        else:
            print("No such student.")
    if option==3:
        break

        
            
