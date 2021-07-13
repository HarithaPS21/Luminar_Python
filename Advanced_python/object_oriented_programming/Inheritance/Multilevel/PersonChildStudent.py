
# Multilevel/Heirarchial Inheritance  - inheriting a class which is inherited by another classs
#                                     - each class acts as a parent as well as a child class simultaneously

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):  #  Child class inherits Person class
    def cvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Student(Child):  #  Student class inherits Child class
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)

ch=Child()
ch.cvalue("Erklm",7)
ch.pvalue("Anju",22)

st=Student()
st.svalue(2,45)
st.cvalue("Kollam",9)
st.pvalue("Akhil",25)
