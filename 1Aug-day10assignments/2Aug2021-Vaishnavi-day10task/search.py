class Student:
    def GetStudent(self):
        self.__rollno = input("Enter Roll No:")
        self.__name = input("Enter Name:")
        self.__physicsMarks = int(input("Enter Physics Marks:"))
        self.__chemistyMarks = int(input("Enter Chemistry Marks:"))
        self.__mathMarks = int(input("Enter Maths Marks:"))
        self.__englishMarks = int(input("Enter English Marks:"))
        self.__computerMarks = int(input("Enter Computer Marks:"))
        return(self.__rollno)

    def PutStudent(self):
        print(self.__rollno,self.__name,((self.__physicsMarks+self.__chemistyMarks+self.__mathMarks)/3))
    def Search(self,min,max):
        per = (self.__physicsMarks+self.__mathMarks+self.__chemistyMarks+self.__englishMarks+self.__computerMarks)/5
        if(per>=min and per<=max):
            return True
        else:
            return False

# creating a dictionary to store student record 
studentDict = dict()
n = int(input("How Many Students you Want To Input?"))
for i in range(n):
 S = Student()
 rollno = S.GetStudent()
 studentDict.setdefault(rollno,S)

# Searching for student records with roll numbers provided by the user.
rollno = input("Enter Roll Number you Want Search?")
S = studentDict.get(rollno,"Not Found!")
if(isinstance(S,Student)):
    S.PutStudent()
else:
    print(S)


print("All students who scored more that 60 percentage are : ")
gradeAStudent = list(filter(lambda s:s.Search(60,100),studentDict.values()))
if(len(gradeAStudent) == 0):
    print("Record Not Found!")
else:
    for S in gradeAStudent:
        S.PutStudent()