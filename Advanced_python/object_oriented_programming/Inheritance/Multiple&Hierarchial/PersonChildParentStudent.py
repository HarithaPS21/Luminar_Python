class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Parent(Person):
    def parvalue(self,phn):
        self.phn=phn
        print(self.phn)
class Student(Child):
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)

ch=Child()
ch.pvalue("Anju",12)
ch.cvalue("Kollam",4)

pa=Parent()
pa.pvalue("Achu",35)
pa.parvalue(9739475654)

st=Student()
st.cvalue("PTA",10)
st.svalue(12,49)
st.pvalue("Anjali",22)
