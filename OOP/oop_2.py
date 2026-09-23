class Employee:
    company_name = "ZeroAI"
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary 
    def display(self):
        print("\nEmployee Name :",self.name)
        print("Employee ID :",self.id)
        print("Employee Salary :",self.salary)
        print("Company Name :",self.company_name)
        print()
e1 = Employee("Kamalesh",101,35000)
e2 = Employee("Akash",102,50000)
Employee.company_name = "OpenAI"
e2.company_name = "Anthropic"
e1.display()
e2.display()
