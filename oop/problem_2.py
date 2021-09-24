class Employee():
    def setvalue(self,name,id,salary,age,company_name,department):
        self.name=name
        self.id=id
        self.salary=salary
        self.age=age
        self.company_name=company_name
        self.department=department
    def printvalue(self):
        print("name",self.name)
        print("id",self.id)
        print("salary",self.salary)
        print("age",self.age)
        print("company name",self.company_name)
        print("department",self.department)

emp=Employee()
emp.setvalue("arya",363910,30000,23,"IBM","development")
emp.printvalue()

