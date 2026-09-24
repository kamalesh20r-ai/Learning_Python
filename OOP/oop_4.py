class Student :
    def __init__(self,name,department,marks):
        self.name = name
        self._department = department 
        self.__marks = marks 
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if new_marks > 0 and new_marks < 100 :
            self.__marks = new_marks
        else :
            print("Invalid Marks")
s1 = Student("Kamalesh","AI&DS",93)
s1.set_marks(98)
print(s1.get_marks())
s1.set_marks(105)
    