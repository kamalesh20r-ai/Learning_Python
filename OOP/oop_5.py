class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Person's Name :",self.name)
        print("Person's Age :",self.age)
class Student(Person):
    def __init__(self,name,age,roll_no,department):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.department = department
    def display_student(self):
        print("Roll No :",self.roll_no)
        print("Deepartment :",self.department)
s1 = Student("Kamalesh",18,101,"AI&DS")
s1.display_student()
s1.display_person()