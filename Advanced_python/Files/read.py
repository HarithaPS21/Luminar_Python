# Reading contents of a file

f1=open("file_operations","r")
# print(f1)                      # prints path/location address of the reference f1
for i in f1:                   # so we have to iterate contents of a file
    print(i)