class Employee:
    def setno(self,sno):
        self.__sno=sno
    def setname(self,name):
        self.__name= name 
    def setcourse(self,course):
        self.__course=course
    def setsalary(self,salary):
        self.__salary=salary
    def getsno(self):
        return self.__sno
    def getname(self):
        return self.__name   
    def getcourse(self):
        return self.__course
    def getsalary(self):
        return self.__salary   
e = Employee()
e.setno(1)
e.setname('thanuja')
e.setcourse('pythondeveloper')
e.setsalary(300000)
print("Employeesno",e.getsno())
print("Employeename",e.getname())
print("Emploeecourse",e.getsno())
print("Employeesalary",e.getname())
