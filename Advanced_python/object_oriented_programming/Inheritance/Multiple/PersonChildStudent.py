

# Multiple Inheritance  -  inheriting attributes and methods of more than one class

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child:
    def cvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Student(Person,Child):    # Multiple inheritance
    def svalue(self,roll,mark):
        self.roll=roll
        self.mark=mark
        print(self.roll,self.mark)

st=Student()
st.pvalue("amal",25)
st.cvalue("Kollam",8)
st.svalue(2,45)