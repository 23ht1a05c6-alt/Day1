class Product:
    def setno(self,sno):
        self.__sno=sno
    def setname(self,name):
        self.__name= name 
    def setcost(self,cost):
        self.__cost=cost
    
    def getsno(self):
        return self.__sno
    def getname(self):
        return self.__name   
    def getcourse(self):
        return self.__cost
      
p = Product()
p.setsno(1)
p.setname('santoor')
p.setcost(500)
print("Productsno",p.getsno())
print("Productname",p.getname())
print("Productcost",p.getcost())

