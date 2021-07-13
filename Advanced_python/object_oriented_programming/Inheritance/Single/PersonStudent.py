# INHERITANCE   -  acquiring attributes and methods of a class by another class
#               -  implemented when multiple classes are used


# Single Inheritance  - inheriting attributes and methods of a single class

class Person:      # Parent class/Base class/Super class
    def pdetails(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Student(Person):          # inheriting Person class by Student class
    def sdetails(self,rollno,dept,mark):
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
        print(self.rollno,self.dept,self.mark)
        print(self.name,"marks is ",self.mark)
# pe=Person()
# pe.pdetails("Anu",23,"Kollam")

st=Student()
st.pdetails("Anu",23,"Kollam")
st.sdetails(12,"CSE",45)





