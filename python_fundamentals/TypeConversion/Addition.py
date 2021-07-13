
# input() function returns strings.
# So if you are expecting a numeric value as output, pass the output of input() function as the input of int() or float()

#                    TYPE CONVERSION FUNCTIONS IN PYTHON :

# int() function converts a string value into integer value
a=int(input("Enter first no. "))
b=int(input("Enter second no. "))
print(a+b)

# float() function converts a string value into floating point number.
c=float(input("Enter a value"))
print(type(c))

# bool() function converts a string into boolean value
c=bool(input("Enter a value"))
print(type(c))    # class <bool>