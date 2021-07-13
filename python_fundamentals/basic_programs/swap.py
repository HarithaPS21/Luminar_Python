# using temp.............................
# num1=int(input("Enter first no."))
# num2=int(input("Enter second no."))
# print("Numbers before swapping:",num1,num2)
# temp=num1
# num1=num2
# num2=temp
# print("Numbers after swapping:",num1,num2)

# second approach..............in python only
num1=int(input("Enter first no."))
num2=int(input("Enter second no."))
print("Values before swapping:",num1,num2)
num1,num2=num2,num2  # (num1,num2)=(num2,num1)
print("Values after swapping: ",num1,num2)

# third approach...........................................
# num1=int(input("Enter first no. "))   # num1=5
# num2=int(input("Enter second no. "))  # num2=2
# print("Value before swapping num1: ",num1,"\nValue before swapping num2: ",num2)
# num1=num1+num2  # num1=7
# num2=num1-num2  # num2=5
# num1=num1-num2  # num1=2
# print("Value after swapping num1: ",num1,"\nValue after swapping num2: ",num2)



