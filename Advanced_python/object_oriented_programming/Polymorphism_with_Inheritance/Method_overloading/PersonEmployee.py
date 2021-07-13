class Person:
    def printDetails(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Employee(Person):
    def printDetails(self,empid,salary,dept):
        self.empid=empid
        self.salary=salary
        self.dept=dept
        print(self.empid,self.salary,self.dept)


pe=Person()
pe.printDetails("Anu",23)

emp=Employee()
emp.printDetails(2,30000,"Finance")
emp.printDetails("Anu",22)