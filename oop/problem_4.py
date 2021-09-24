class Student:
    def setvalue(self,name,roll_no,division,school):
        self.name=name
        self.roll_no=roll_no
        self.division=division
        self.school=school
    def printvalue(self):
        print(self.name,self.roll_no,self.division,self.school)

stu=Student()
stu.setvalue("arya",30,"A","vidya")
stu.printvalue()
