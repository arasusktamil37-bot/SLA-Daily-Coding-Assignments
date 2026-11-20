class Student:
    def __init__(self):
        self.__mark = 0
    def set_marks(self):
        Student_mark = int(input("ENTER THE MARK OF STUDENT 1 : "))
        mark = Student_mark
        if mark >= 0 and mark <= 100:
            self.__mark = mark
            print("THE MARK HAS BEEN UPDATED !!")
            self.get_marks()
        else :
            print("THE ENTERED MARK IS INVALID !!")
    def get_marks(self):
        print(f"STUDENT MARK IS {self.__mark}")

Totalmark = Student()
Totalmark.set_marks()
            
