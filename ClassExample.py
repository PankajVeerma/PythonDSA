class Employee:
    def __init___(self,empid=None,empname=None,empsalary=None):
        self.empid=empid
        self.empname=empname
        self.empsalary=empsalary
    def setEmpid(self,empid):
        self.empid =empid
    def setEmpname(self,empname):
        self.empname =empname
    def setEmpsalary(self,empsalary):
        self.empsalary =empsalary
    def getEmpid(self):
        return self.empid 
    def getEmpname(self):
        return self.empname
    def getEmpsalary(self):
        return self.empsalary 
            
e1=Employee()   
e2=Employee(1001,"Rahul",200000) 

e1.setEmpid(100)
e1.setEmpsalary(30000)
e1.setEmpname("Abhishek")
print(e1.getEmpid(),e1.getEmpname(),e1.getEmpsalary())
print(e2.getEmpid(),e2.getEmpname(),e2.getEmpsalary)