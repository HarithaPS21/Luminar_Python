
# Polymorphism  -  having many forms

# Method overloading  - same method name but different number of arguements..........not supported in Python
#                     - based on the no. of values passed, method selected
#                     - the method with the same no. of arguements as the no. of values passed is executed
#                     - the latest created method executed in Python

class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
    def num(self,n3):
        self.n3=n3
        print(self.n3)
op=Operators()
op.num(3)
op.num(2,3)      # error................method overloading not supported in Python