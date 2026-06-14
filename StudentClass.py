class Student:
    #? cunstructor
    #! its automatically called object is created
    numberOfStudent = 0
    schoolName = "SRGC"

    def __init__(self,name,rollNumber,marks):
        #? Data or members
        self.name = name
        self.rollNumber = rollNumber
        #? Access modifier private
        self.__marks = marks
        self.numberOfStudent = Student.numberOfStudent + 1
        Student.numberOfStudent = Student.numberOfStudent + 1
    #? Methods 
    def study(self):
        # print(f'id of study:-{id(self)}')
        print(f"I am {self.name} and I am studing")
        
    def play(self):
        # print(f'id of play:-{id(self)}')
        print(f"Now {self.name} going to play")

s1 = Student("Shahid",1,90)
s2 = Student("Goku",2,50)
print(Student.schoolName)
print((s1.numberOfStudent,s2.numberOfStudent))
print(s1.__marks)
s1.__marks = 80
print(s1.marks)

