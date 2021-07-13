
# EXCEPTION HANDLING IN PYTHON.......................HANDLING UNEXPECTED ERRORS USING TRY AND EXCEPT BLOCKS

# EXCEPTIONS  -  unexpected errors while running code
#             -  due to user input
#             -  try,except,finally  blocks
# try         -  the piece of code which raises an exception is written in the try block..................runs always
# except      -  catches errors...........................runs only if an exception occurs
#             -  the action to be performed if an error occurs is given in the except block
# finally     -  to leave a message................runs always

num1=int(input("Enter first no  "))
num2=int(input("Enter second no  "))
try:                       # try block works always...........condition checking
    print("hello")
    print(num1/num2)
except Exception as e:    # works only if an error occurs..........otherwise goes to finally block
    print("Exception occured",e)
finally:              # works always after the other blocks...........at last
    print("inside finally")