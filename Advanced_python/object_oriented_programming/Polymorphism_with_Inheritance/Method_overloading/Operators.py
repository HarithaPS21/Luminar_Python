# Polymorphism  -  having many forms

# Method overloading  - same method name but different number of arguements..........not supported in Python
#                     - based on the no. of values passed, method selected
#                     - the method with the same no. of arguements as the no. of values passed is executed

class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
class Display(Operators):             # single inheritance...........acts as a single class
    def num(self,n3):
        self.n3=n3
        print(self.n3)

d=Display()
d.num(3)
# d.num(3,2)  ................error
