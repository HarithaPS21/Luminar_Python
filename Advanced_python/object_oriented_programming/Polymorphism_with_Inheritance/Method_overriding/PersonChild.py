class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
        print("inside parent class method")
class Child(Person):
    def pvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
        print("inside child class")


ch=Child()
ch.pvalue("Akhil",23)         # child class method executed
ch.pvalue("Kollam",8)         # child class method executed