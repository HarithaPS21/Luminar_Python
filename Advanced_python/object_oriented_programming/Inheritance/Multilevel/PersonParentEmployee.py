class Person:
    def perdetails(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def pardetails(self,adrs,phn):
        self.adrs=adrs
        self.phn=phn
        print(self.adrs,self.phn)
class Employee(Parent):
    def empdetails(self,empid,salary,dept):
        self.empid=empid
        self.salary=salary
        self.dept=dept
        print(self.empid,self.salary,self.dept)

par=Parent()
par.perdetails("Anu",23)
par.pardetails("Kollam",9746537202)

emp=Employee()
emp.perdetails("Akhil",25)
emp.pardetails("Erklm",9384740850)
emp.empdetails(2,40000,"Finance")
