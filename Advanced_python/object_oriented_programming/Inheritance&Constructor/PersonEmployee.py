class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,empid,salary,dept,name,age):  # include all attributes of parent class constructor
        self.empid=empid
        self.salary=salary
        self.dept=dept
        super().__init__(name,age)      # calling parent class constructor using super() keyword
    def empdetails(self):
        print(self.empid,self.salary,self.dept)

emp=Employee("002",40000,"Finance",'Akhil',23)   # give all attributes of Student class constructor
emp.printval()
emp.empdetails()