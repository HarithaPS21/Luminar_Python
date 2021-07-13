
# Method overriding  - same method name and same no. of arguements..........supported in Python
#                    - the child class method overrides the parent class method
#                    - the child class method is executed......parent class method never executed
#                    - only the latest created method executed in Python

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print("inside parent class method")
    def pvalue(self,mark,salary):
        self.salary=salary
        self.mark=mark
        print("inside child class method")

pe=Person()
pe.pvalue("Anu",23)         # child class method executed
pe.pvalue(45,50000)         # child class method executed