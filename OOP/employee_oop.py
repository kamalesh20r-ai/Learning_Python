class Employee :
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    def display(self):
        print("\nEmployee Name :",self.name)
        print("Employee ID :",self.id)
        print("Employee Salary :",self.salary)
e1 = Employee("Kamalesh",101,35000)
e2 = Employee("Kabilan",102,45000)
e1.display()
e2.display()