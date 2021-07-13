# division of two numbers
def zeronotrequired(func):  # div(1,0)
    def wrapper(num1,num2): # (1,0)
        if (num1==0) | (num2==0): # num2==0
            raise Exception("cannot divide by zero")  # to generate customized exceptions
        return func(num1,num2)
    return wrapper
def decorator_div(func):             # div(5,10)
    def wrapper(num1,num2):          # (5,10)
        if num1<num2:                # 5<10
            (num1,num2)=(num2,num1)  # 10,5
        return func(num1,num2)       # div(10,5)
    return wrapper
@zeronotrequired
@decorator_div
def div(num1,num2):
    return num1/num2                 # 10/5=2
try:
    print(div(1,0))
except Exception as e:
    print(e)
