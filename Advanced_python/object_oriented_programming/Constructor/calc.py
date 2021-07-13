class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2

num1=int(input("Enter a no."))
num2=int(input("Enter a no. "))
calc=Calculator(num1,num2)
next=1
while next:
    ch=int(input("press \n1.Addition \n2.Subtraction\n3.Multiplication\n4.Division\n"))
    if ch==1:
        print(calc.add())
    elif ch==2:
        print(calc.sub())
    elif ch==3:
        print(calc.mul())
    elif ch==4:
        print(calc.div())
    else:
        print("Please enter a valid choice")
    next=int(input("Do yo want to continue? press 0 to exit "))