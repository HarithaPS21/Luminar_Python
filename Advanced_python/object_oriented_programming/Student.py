class Student:
    def setval(self,name,roll,mark,school_name):
        self.name=name
        self.roll=roll
        self.mark=mark
        self.school_name=school_name
        print("Name: ",name)
        print("ROLL No: ",roll)
        print("Mark: ",mark)
        print("School Name: ",school_name)
st=Student()
st.setval("Manu",20,45,"Little Flower")

st2=Student()
st2.setval("Haritha",12,48,"Little Flower")
# can optionally define schoolname as a static variable at the top since "luminar" is repeated