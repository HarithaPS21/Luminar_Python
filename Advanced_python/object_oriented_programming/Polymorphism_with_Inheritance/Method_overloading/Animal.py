class Animal:
    def walk(self,color):
        self.color=color
        print(self.color)
        print("animal walking......")
class Dog:
    def bark(self):
        print("barking...")
    def walk(self,breed,name):
        self.breed=breed
        self.name=name
        print(self.breed,self.name)
        print("dog walking...")
an=Animal()
an.walk("Black")

d=Dog()
d.walk("Pomeranian","Elsa")
d.walk("Gold")


