from functools import reduce
lst=[1,2,3,4,5,6]
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)