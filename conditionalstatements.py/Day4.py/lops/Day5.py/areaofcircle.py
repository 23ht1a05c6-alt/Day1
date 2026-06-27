#quartic equations
'''

a = int(input("give a:"))
b = int(input("give b:"))
c = int(input("give c:"))
root1 = 0
root2 = 0
d = (b**2) - 4*a*c #-b+-(b**2-4*a*c)1/2
root1 = (-b+(d**(0.5)))/2*a
root2 = (-b+(d**(0.5)))/2*a
print(f"roots:({root1},{root2})")


------------


#without useing temp variable can swap the numbers
a = int(input("give a number"))
b = int(input("give b number"))
b = b+a
a = b-a
b = b-a
print(f"value ofa:{a}")
print(f"value ofb:{b}")


-------------


a = int(input("give a value"))
b = int(input("give b value"))
temp = a
a = b
b = temp
print(f"value a is:{a}")
print(f"value b is:{b}")
-------------
a ="ratna"
print(a.startswith("a"))


a = int(input("give a value"))
b = int(input("give b value"))
a = a+b #a = 20 ,b = 10 a+b= 30 a = 30
a = a-b #30-10=20
b = b-a #b=10-20=-10
print(f"value a is:{a}")
print(f"value b is:{b}")

------------
def area_of_circle(radius):
    area = 3.14*radius**2
    return area
r = float(input("enter radius:"))
print(f"Area of circle:{area_of_circle(r)}")

def simple_interset(p,r,t): #si=p*r*t/100
    si = (p*r*t)
    return si
p = float(input("enter principal Amount:"))
r = float(input("enter rate of Interset:"))
t = float(input("enter time:"))
print("simple interset=",(p,r,t))

------------


#fuction Definition
def student_Details(name,age,course): #with parameter and with retrn type
    
    print(f"student name:{name}")
    print(f"student age:{age}")
    print(f"student course:{course}")
student_Details("tanu", 21,"python")    
-------------


def student_Details(name,age,course): #with parameter and with retrn type
    Details = (name{name},age(age),course(course))
    return Details
result= student_Details("tanu",21,"python")   
print(result)  
'''
--------------

def show(*x):
   
    print(x)
 
show(40,)  





