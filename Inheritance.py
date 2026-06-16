
class User:
    # def __init__(self, Name, id):
    #     self.Name = Name
    #     self.id = id
    def login(self):
        print("P Logged in")
    def logout(self):
        print("P Logged Out")

class Student(User):
    # def login(self):
    #     print("S logged in")
    pass
s1 = Student()
s1.login()
s1.logout()
# s1.logout()
s2 = User()
s2.login()