class Person:
    def __init__(self,name):
        self.name = name 
    def display_person(self):
        print("Person Name :",self.name)
class Employee(Person):
    def __init__(self, name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    def display_employee(self):
        print("Employee ID",self.employee_id)
class Manager(Employee):
    def __init__(self, name, employee_id,department):
        super().__init__(name, employee_id)
        self.department = department
    def display_manager(self):
        print("Department :",self.department)
emp = Manager("Kamalesh",101,"AI&DS")
emp.display_person()
emp.display_employee()
emp.display_manager()
    
        