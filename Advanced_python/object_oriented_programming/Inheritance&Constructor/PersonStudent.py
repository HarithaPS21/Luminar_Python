class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):     # add attributes of parent class constructor also
        super().__init__(name, age)              # calling parent class constructor using super() keyword
        self.rollno=rollno
        self.mark=mark
    def printval(self):
        print(self.rollno,self.mark)

st=Student(2,45,"anu",23)                        # give all attributes of student class
st.print()
st.printval()