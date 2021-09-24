class Employee:
    company="company IBM"
    def setvalue(self,name,id,role):
        self.name=name
        self.id=id
        self.role=role
    def printvalue(self):
        print("name",self.name)
        print("id",self.id)
        print("role",self.role)
        print(Employee.company)
em1=Employee()
em1.setvalue("arya",402,"HR")
em1.printvalue()
em2=Employee()
em2.setvalue("anu",403,"manager")
em2.printvalue()