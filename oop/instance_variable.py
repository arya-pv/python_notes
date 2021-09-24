#...oop....
#instance variable
#static variable


#...instance variable...related to methods...(self.variable)
#....static variable...it is given inside class..related to class

class Student:
    school="luminar"     #this is static variable
    def setvalue(self,name,roll_no):
        self.name=name                #this is instance variable
        self.roll_no=roll_no

    def printvalue(self):
        print("name",self.name)
        print("school",Student.school)
        print("roll no",self.roll_no)

stu1=Student()
stu1.setvalue("arya",30)
stu1.printvalue()
stu2=Student()
stu2.setvalue("anu",45)
stu2.printvalue()