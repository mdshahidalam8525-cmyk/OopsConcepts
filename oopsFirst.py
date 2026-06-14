
# ? Create a cunstructor
# class Student:

#     #! cunstructor
#     def __init__(self):
#         print(id(self))
#         print("i will get call auto matically:")

# s1 = Student()
# print(id(s1))


# ? Creating objects of a class
# class Student:
#     #? cunstructor
#     #! its automatically called object is created
#     def __init__(self):
#         self.name = "shahid"
#         self.rollNumber = 1
#         self.marks = 90
        

# s1 = Student()
# print(s1.name)
# print(s1.rollNumber)
# print(s1.marks)


# # ? Creating objects of a class and user define by terms
# class Student:
#     #? cunstructor
#     #! its automatically called object is created
#     def __init__(self,name,rollNumber,marks):
#         #? Data or members
#         self.name = name
#         self.rollNumber = rollNumber
#         self.marks = marks
#     #? Methods
#     def study():
#         print("I am studing")
        
#     def play():
#         print("Now i'm going to play")

# s1 = Student("Shahid",1,90)
# print(s1.name)
# print(s1.rollNumber)
# print(s1.marks)
# s2 = Student("Goku",2,50)
# print(s2.name)
# print(s2.rollNumber)
# print(s2.marks)


#? Nmw we can add methods
# ? Creating objects of a class and user define by terms
class Student:
    #? cunstructor
    #! its automatically called object is created
    def __init__(self,name,rollNumber,marks):
        #? Data or members
        
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks
    #? Methods 
    def study(self):
        # print(f'id of study:-{id(self)}')
        print(f"I am {self.name} and I am studing")
        
    def play(self):
        # print(f'id of play:-{id(self)}')
        print(f"Now {self.name} going to play")

s1 = Student("Shahid",1,90)
# print(f'id of s1:-{id(s1)}')
s1.study()
s1.play()
s2 = Student("Goku",2,50)
# print(f'id of s2:-{id(s2)}')
s2.study()
s2.play()

print('Hallo')