

# def printPerson(wlocation,hlocation):
#     print(wlocation,hlocation)
# printPerson("kakkanad","thrissur")

def printPerson(**kwargs):
    print(kwargs["wlocation"])
    print(kwargs["hlocation"])
printPerson(wlocation="kakkanad",hlocation="thrissur")