min=int(input("Enter initial range"))
max=int(input("Enter final range "))
print("Even numbers between",min,"and",max,"are\n")
for num in range(min,max+1):
    if num%2==0:
        print(num)