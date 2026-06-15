class Student:
    #? cunstructor
    #! its automatically called object is created
    #! private
    #? class veriable and ststic propeties
    __numberOfStudent = 0
    __schoolName = "SRGC"
    
    def __init__(self,name,rollNumber,marks):
        #? Data or members
        self.name = name
        self.rollNumber = rollNumber
        #? Access modifier private
        self.__marks = marks
        self.numberOfStudent = Student.__numberOfStudent + 1
        Student.__numberOfStudent = Student.__numberOfStudent + 1
    #? Access private objects 
    #! getter 
    def getMarks(self):
        return self.__marks
    #? static Method
    #? changes access some cases
    #! setter
    def setMarks(self,newMarks, passCode):
        if (passCode == self.__auth()):
            self.__marks = newMarks
        else:
            print("Your not abale to change marks! ")
    #! getter2
    def getSchoolName():
        return Student.__schoolName
    #? school name for student 
    def studentSchoolName(self):
        return Student.__schoolName
    #! setter2
    def setSchool(newSchool,passcode):
        Student.sendMail()
        Student.__schoolName = newSchool

    def sendMail():
        print("School Name changed SRGC -> ICKK ")
        
    #? give authentication
    def __auth(self):
        return '0000'
    
    #? Methods 
    def study(self):
        # print(f'id of study:-{id(self)}')
        print(f"I am {self.name} and I am studing")
        
    def play(self):
        # print(f'id of play:-{id(self)}')
        print(f"Now {self.name} going to play")

s1 = Student("Shahid",1,90)
s2 = Student("Goku",2,50)
print(Student.getSchoolName())
print(s1.studentSchoolName())
Student.setSchool('ICKK','0000')
print(s1.studentSchoolName())
print((s1.numberOfStudent,s2.numberOfStudent))
# s1.marks = 45 
# print(s1.marks)
# print(s1.getMarks())
# print(s1.__auth())
# s1.setMarks(95,'0001')
# print(s1.getMarks())
