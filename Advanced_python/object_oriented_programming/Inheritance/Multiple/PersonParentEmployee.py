class Person:
    def perDetails(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent:
    def parDetails(self,adrs,phn):
        self.adrs=adrs
        self.phn=phn
        print(self.adrs,self.phn)
class Employee(Person,Parent):
    def empDetails(self,id,salary,desig):
        self.id=id
        self.salary=salary
        self.desig=desig
        print(self.id,self.salary,self.desig)



emp=Employee()
emp.perDetails("Anju",23)
emp.parDetails("Kollam",9744987895)
emp.empDetails(2,45000,"Developer")
