employees={
1000:{"eid":1000,"ename":"ajay","salary":34000,"Designation":"developer"},
1001:{"eid":1001,"ename":"arun","salary":38000,"Designation":"developer"},
1002:{"eid":1002,"ename":"akhil","salary":21000,"Designation":"hr"},
 1003:{"eid":1003,"ename":"anu","salary":45000,"Designation":"Analyst"}
}

id=int(input("enter an id "))  # input through output
if id not in employees:
    print("invalid id")
else:
    prop=input("enter the property you want to print: 1.ename 2.salary 3.Designation ")
    if prop not in employees:
        print("The property you entered doesn't exist")
    else:
        print(employees[id][prop])