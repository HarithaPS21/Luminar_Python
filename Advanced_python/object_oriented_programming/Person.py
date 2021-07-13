class Person:
    def setval(self,name,age):  # method 1
        self.name=name          # instance variable
        self.age=age            # instance variable

    def printval(self):         # method 2
        print("Name : ",self.name)
        print("Age : ",self.age)
pe=Person()
pe.setval("Anu","24")
pe.printval()