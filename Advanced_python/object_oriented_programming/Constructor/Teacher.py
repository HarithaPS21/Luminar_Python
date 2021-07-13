class Teacher:
    college_name='College of Engineering Kidangoor'
    def __init__(self,name,tid,dept,sub):
        self.name=name
        self.tid=tid
        self.dept=dept
        self.sub=sub
    def printdetails(self):
        print("Name: ",self.name)
        print("ID: ",self.tid)
        print("Department: ",self.dept)
        print("Subject: ",self.sub)
te=Teacher("Shandry","003","CSE","CSA")
te.printdetails()