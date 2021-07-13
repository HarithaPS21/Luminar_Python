
# Copying contents of a file to another

f1=open("book","r")
f2=open("bookcopy","w")
for i in f1:
    f2.write(i)