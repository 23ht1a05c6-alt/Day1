'''
class Triangle:
    def area(self):
        return  0.5*self. base*self.height
t = Triangle()
print("Area of trianle")
t.base = float(input("enter base"))
t.height = float(input("enter height"))

  


class Employee:
    def display(self):
        self.names = input("enter a names")
        self.ids = input("enter a ids")
        self.professions = input("enter a professions") 
e = Employee()
e.display()
   
  



class Animal:
     
    def eat(self):
        print("animal are eating")
class Dog(Animal):
   
    def brak(self):
        print("Dog is braking") 
        
d = Dog() 

d.eat()
d.brak()  

 


class Person:
    def name(self):
        print("name is tanuja")
class Student(Person):
    def marks(self):
        print("student marks is 90")
        print("student id is 101")
        print("student brnch is 101")
s = Student()
s.name()
s.marks()




class Grandfather:
    def home(self):
        print("grandfather's home")
class Father(Grandfather):
    def car(self):
        print("father's car")
class Daugther(Father):
    def bike(self) :
        print("daugther's bike")
d = Daugther()
d.home()
d.car() 
d.bike()              
'''
                