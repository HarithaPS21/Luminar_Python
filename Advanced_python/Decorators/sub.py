
# Decorators  - to decorate functions
#             - to add extra features to a function without changing the function definition
def decorator_sub(func):          # sub(2,10)
    def wrapper(num1,num2):       # (2,10)
        if num1<num2:             # 2<10
            num1,num2=num2,num1
        return func(num1,num2)    # func(10,2)
    return wrapper
@decorator_sub
def sub(num1,num2):
    return num1-num2              # 10-2=8
print(sub(2,10))