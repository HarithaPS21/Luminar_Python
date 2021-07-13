class Employee:
    def setval(self,name,id,salary,company):
        self.name=name
        self.id=id
        self.salary=salary
        self.company=company
    def printval(self):
        print("\nName : ",self.name)
        print("id : ",self.id)
        print("Salary : ",self.salary)
        print("Company : ",self.company)
emp=Employee()
emp.setval("Anu","001","30000","Luminar Technolab")    #  since printval() depends on setval()......called first
emp.printval()

emp2=Employee()
emp2.setval("Amal","002","20000","Luminar")
emp2.printval()
