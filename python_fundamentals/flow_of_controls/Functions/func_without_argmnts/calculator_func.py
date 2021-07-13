def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("Select an operation\n1.Addition\n2.Subtracion\n3.Multiplication\n4.Division")
ch = int(input("Enter your choice "))
num1 = float(input("Enter a number "))
num2 = float(input("Enter a number "))
if ch==1:
    print(add(num1,num2))
elif ch==2:
    print(sub(num1,num2))
elif ch==3:
    print(mul(num1,num2))
elif ch==4:
    print(div(num1,num2))
else:
    print("please enter a valid choice")
