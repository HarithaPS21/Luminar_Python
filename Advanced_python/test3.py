f1 = open("test3", "r")
employees = {}
for line in f1:
    words = line.rstrip("\n").split(",")
    # print(words)
    id = words[0]
    name = words[1]
    desig = words[2]
    exp = words[3]
    salary = words[4]

    employees[id] = {"id": id, "name": name, "desig": desig, "exp": exp, "salary": salary}
# print(employees)

        # dict[id] = {}

        # dict.update({emp["id"]:emp})
        # d.update(d1{id:})
        # print(d)
        # dict[id]=dict.update({})
        # dict.update({id:{"id":id,"name":name,"desig":desig,"exp":exp,"salary":salary},})
for k, v in employees.items():
    print(k,v)




