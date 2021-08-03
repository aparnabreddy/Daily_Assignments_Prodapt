class Student:
    marks = []
    def getData(self, rn, name,adminno, m1, m2, m3,m4,m5):
        Student.rn = rn
        Student.name = name
        Student.adminno=adminno
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        Student.marks.append(m4)
        Student.marks.append(m5)
      
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        print ("Admin No: ", Student.adminno)
        #print ("Marks in subject 1: ", Student.marks[0])
        #print ("Marks in subject 2: ", Student.marks[1])
        #print ("Marks in subject 3: ", Student.marks[2])
        #print ("Marks in subject 4: ", Student.marks[3])
        #print ("Marks in subject 5: ", Student.marks[4])
        print ("Marks are: ", Student.marks)
        print ("Total Marks are: ", self.total())
        print ("Average Marks are: ", self.average())
        
    def total(self):
        return (Student.marks[0] + Student.marks[1] +Student.marks[2] +Student.marks[3] +Student.marks[4])
    
    def average(self):
        return ((Student.marks[0] + Student.marks[1] +Student.marks[2] +Student.marks[3] +Student.marks[4])/5)
    
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
Adminno= int( input("Enter the Admin number: "))
m1 = int (input("Enter the marks in 1st subject: "))
m2 = int (input("Enter the marks in 2nd subject: "))
m3 = int (input("Enter the marks in 3nd subject: "))
m4 = int (input("Enter the marks in 4nd subject: "))
m5 = int (input("Enter the marks in 5nd subject: "))

s1 = Student()
s1.getData(r, name, Adminno, m1, m2, m3, m4, m5)
s1.displayData()

# while(1):
#     print("1.Add Student Details")
#     print("2.Search Student Using RollNo:")
#     print("3.Student Api:")
#     print("4.Print Student Based On Rank:")
#     print("5.exit")
#     option=int(input("Enter your option:"))
#     if option==1:
#         displayData()

# stud_dict = dict()
# stud_dict[r] = name,Adminno
# srn = int(input("Enter the roll number of the student whose details you'd like to view: "))
# if srn in stud_dict:
#     print(stud_dict[srn])
# else:
#     print("No such student.")

