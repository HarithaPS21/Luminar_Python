class Student:
    school_name='Little Flower Public School'
    def setval(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark
        print("Name: ",name)
        print("ROLL No: ",roll)
        print("Mark: ",mark)
        print("School Name: ",Student.school_name)
st=Student()
st.setval("Manu",20,45)

st2=Student()
st2.setval("Haritha",12,48)