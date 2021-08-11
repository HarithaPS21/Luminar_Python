f1=open("test3","r")
# employees={1000:{"id":1000,"name":"Ajay","desig":"developer","exp":2,"salary":25000}}
employees={}
for line in f1:
    # print(line)
    eid,name,desig,exp,salary=line.rstrip("\n").split(",")
    employees[int(eid)]={"eid":eid,"name":name,"desig":desig,"exp":exp,"salary":salary}
print(employees)

def printEmployee(id=None,**kwargs):
    if id in employees:
        print(employees[id]["name"])
        if "prope" in kwargs:
            if kwargs["prope"] in employees[id]:
                print(employees[id][kwargs["prope"]])
            else:
                print("invalid property")
    else:
        print("invalid id")
        # raise Exception("invalid id")



#
#
# try:
#     id=int(input("Enter id "))
#     printEmployee(id)
#     prop=input("Enter a property ")
#     printEmployee(id,prope=prop)
# except Exception as e:
#     print("Exception occured- invalid id",e)
#     print("Please check the id you entered")
# except:
#     print("Exception occured-invalid property")
#     print("Please enter a valid property")
printEmployee(id=1007,prope="dept")