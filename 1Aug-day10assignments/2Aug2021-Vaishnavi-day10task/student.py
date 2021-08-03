class Student: 
    def __init__(self):
        self.name = input("Enter student name: ")
        self.rollno = input("Enter student roll number: ")

    def displayStudent(self):
        print("Student Name: ", self.name)
        print("Student Roll Number: ",
        self.rollno)

class Marks:
    def __init__(self):
        self.m1 = int(input("Enter marks in Physics: "))
        self.m2 = int(input("Enter marks in Chemistry: "))
        self.m3 = int(input("Enter marks in Maths: "))
        self.m4 = int(input("Enter marks in English: "))
        self.m5 = int(input("Enter marks in Computer: "))

    def displayMarks(self):
        print("Marks in Physics: ", self.m1)
        print("Marks in Chemistry: ", self.m2)
        print("Marks in Maths: ", self.m3)
        print("Marks in English: ", self.m4)
        print("Marks in Computer: ", self.m5)

class Result(Student, Marks):   

    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)
        self.total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        self.percentage = self.total/5

    def displayResult(self):
        print("Result of ", self.name, " - ", 
        self.rollno)
        print("Total Marks: ", self.total)
        print("Percentage: ", self.percentage)
    

r = Result( ) 
                
r.displayStudent( )                               
r.displayMarks( )               
r.displayResult( )