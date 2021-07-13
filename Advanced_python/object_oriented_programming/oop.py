# class -  design pattern/blueprint
#       -  has similar attributes and methods.........eg.Television,Student...
# self  -  instance keyword
# object -  real world entity............eg.Samsung,iBell,.....
# reference  - location to perform operations on objects......eg.Remote control

# eg. Television     - Class ,
#     Samsung,iBell  - Objects ,
#     Remote control - Reference


class Person:          #  class definition
    def walk(self):    #  method 1
        print("\nPerson is walking")
    def talk(self):    #  method 2
        print("Person is talking")
obj1=Person()
obj1.walk()
obj1.talk()

obj2=Person()
obj2.walk()
obj2.talk()