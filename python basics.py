#variables
#variable is container its strore the data
#golbal variable
#instances
#varible nothing but vars or modifier or send the ValueError
#variable is a temparay stroreage location store te the value
#it takes the latest value
x = "tanu"
print(x)
#variables classified into four types
#global
#local
#class
#instances
#global variables:


#global variable:
#the variable which are decalre outside function are class
#the scope of the global variable is entire program means we can access any where in a program
x = 10
def show():

    print(x)
show()
print(x)
#output:
#10
#10


#local variable
def show():
    x = 10
    print(x):
show()
print(x)    
#the variables which are declare inside function are method are called local variable
#the scope of the local varible with function
def show():
    
    x = 10
    print(x)
show()
print(x)
#output
#10
#nameerror:name
#by useing global keyword we can decare a function



def show():
    global x#key word
    x = 10
    print(x)
show()
print(x)



#class variable
class Sample:
    x = 10
    print(x)
print(Sample.x) 
#the variable which are decakre inside class outside
# we access class variable outside   


#instances
class Sample:
    def show(self):
        self.x = 10
        print(self.x)
s = Sample()
s.show()
print(s.x)


#the variable which are decalre self refer
#we acces instances variable in objects

#rules
#must be start with
#wec cannot decalre keywords an variable name
#valid        invalid              1x
#x            1x
#def

#how to take dynamic vakues
#by using input function it takes the dynamic values key
#by default input function take as string fomate so we translate into your own type casting
a = int(input('enter a num'))

b = int(input('enter b num'))
c = a+b
print(c)
#write a program to calculate simple interset
#area of triangle
#calculate volume of cube
#to print student details
#employee details
#


class Sample:
    name = "tanu"
    print(name)
print(Sample.name)
      


