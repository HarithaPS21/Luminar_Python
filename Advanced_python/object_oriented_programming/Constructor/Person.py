# Constructor  - to initialize instance variables
#              - automatically invoke when creating an object



class Person:
    def __init__(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
    def printval(self):
        print(self.name,self.age,self.adrs)
name=input("Enter name ")
pe=Person(name,24,"Kollam")               # object creation and initialization using constructor
pe.printval()