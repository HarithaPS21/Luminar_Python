from functools import reduce
lst=[1,2,3,4,5,6,7]
largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)

# largest=reduce(lambda num1,num2:num1 if num1>num2 else num2 if num2>num1 else num,lst)
# print(largest)


