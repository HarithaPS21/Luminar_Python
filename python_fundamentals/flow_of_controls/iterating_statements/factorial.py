

# 5! = 5*4*3*2*1 =120

num=int(input("Enter a number "))
fact=1
if num>=0:
    for i in range(1,num+1):
        fact*=i
    print("Factorial of",num,"is",fact)
else:
    print("please enter a positive number")