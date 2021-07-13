# Exception  2  - index out of range error.................when the user tries to access an element not present
a=[1,2,3,4]
b=int(input("Enter an index position "))
try:
    print(a[b])                               # accessing element at index
except Exception as e:
    print("Exception occured ",e)             # list index out of range error
finally:
    print("inside finally")