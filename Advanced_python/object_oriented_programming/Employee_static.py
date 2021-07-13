class Employee:
    company='Luminar Technolab'              # company name defined as a Static variable
    def setval(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def printval(self):
        print("\nName : ",self.name)
        print("id : ",self.id)
        print("Salary : ",self.salary)
        print("Company : ",Employee.company)
emp=Employee()
emp.setval("Anu","001","30000")    #  since printval() depends on setval()......called first
emp.printval()

emp2=Employee()
emp2.setval("Amal","002","20000")
emp2.printval()