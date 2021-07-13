# Single Inheritance  - inheriting attributes and methods of a single class

class Person:                         #  parent class/base class/super class
    def pdetails(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Employee(Person):                #  child class/derived class/subclass
    def empdetails(self,empid,dept,salary):
        self.empid=empid
        self.dept=dept
        self.salary=salary
        print("Employee ID: ",empid,"\nDepartment :",dept,"\nSalary :",salary)
        print("salary of ",self.name,"is ",self.salary)
pe=Person()
pe.pdetails("Akhil",25,"Kollam")              #  own methods

emp=Employee()
emp.pdetails("Akhil",25,"Pathanamthitta")     #  using methods of parent class
emp.empdetails(2,"testing",25000)